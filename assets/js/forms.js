/**
 * CraftEgon Corporate Services — High-Converting Lead Capture & Automation Engine
 * ==============================================================================
 * Centralizes all form submissions, Indian phone validation, lead payload dispatching,
 * webhook integration, localStorage fail-safe persistence, and WhatsApp service prefilling.
 *
 * @module CCSForms
 * @version 2.0.0
 */

'use strict';

/* ── Indian States Constant ─────────────────────────────────── */
const INDIAN_STATES = [
    'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chhattisgarh',
    'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jharkhand', 'Karnataka',
    'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya',
    'Mizoram', 'Nagaland', 'Odisha', 'Punjab', 'Rajasthan', 'Sikkim',
    'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand',
    'West Bengal', 'Delhi', 'Jammu & Kashmir', 'Ladakh', 'Puducherry', 'Chandigarh'
];

/* ============================================================
   CCSForms Namespace
   ============================================================ */
const CCSForms = (function () {

    /**
     * Retrieves runtime configuration safely
     */
    function _getConfig() {
        return window.CCS_CONFIG || {
            whatsAppNumber: '918606918247',
            webhookUrl: '/api/lead-capture',
            webhookTimeoutMs: 6000,
            localStorageKey: 'ccs_lead_intakes',
            callbackPromiseMinutes: 10
        };
    }

    /**
     * Reads UTM tracking parameters
     */
    function _getUtmParams() {
        const params = new URLSearchParams(window.location.search);
        return {
            utm_source: params.get('utm_source') || '',
            utm_medium: params.get('utm_medium') || '',
            utm_campaign: params.get('utm_campaign') || '',
            utm_content: params.get('utm_content') || '',
            utm_term: params.get('utm_term') || ''
        };
    }

    /**
     * Safe query helper
     */
    function _q(form, selector) {
        try { return form.querySelector(selector); } catch (e) { return null; }
    }

    /**
     * Normalizes an Indian phone number to 10 clean digits
     */
    function normalizeIndianPhone(phoneStr) {
        if (!phoneStr) return '';
        let digits = String(phoneStr).replace(/\D/g, '');
        // Remove leading country code +91 or 91 if 12 digits
        if (digits.length === 12 && digits.startsWith('91')) {
            digits = digits.slice(2);
        }
        // Remove leading 0 if 11 digits
        if (digits.length === 11 && digits.startsWith('0')) {
            digits = digits.slice(1);
        }
        return digits;
    }

    /**
     * Displays a clean inline error message below the field
     */
    function showFieldError(field, message) {
        if (!field) return;
        field.classList.add('border-rose-500', 'focus:ring-rose-500', 'bg-rose-50/50');
        field.classList.remove('border-slate-200', 'border-slate-300');

        // Remove existing error message
        const parent = field.parentElement;
        const prev = parent.querySelector('.ccs-form-error');
        if (prev) prev.remove();

        const err = document.createElement('p');
        err.className = 'ccs-form-error text-[11px] font-bold text-rose-600 mt-1 flex items-center gap-1';
        err.setAttribute('role', 'alert');
        err.innerHTML = `<span aria-hidden="true">⚠️</span> <span>${message}</span>`;
        parent.appendChild(err);
    }

    /**
     * Clears all validation errors inside a form
     */
    function clearErrors(form) {
        form.querySelectorAll('.ccs-form-error').forEach(el => el.remove());
        form.querySelectorAll('input, select, textarea').forEach(f => {
            f.classList.remove('border-rose-500', 'focus:ring-rose-500', 'bg-rose-50/50');
            f.classList.add('border-slate-200');
        });
    }

    /**
     * Extracts unified lead intake payload
     */
    function captureFields(form) {
        const utm = _getUtmParams();
        const get = selector => {
            const el = _q(form, selector);
            return el ? el.value.trim() : '';
        };

        const rawPhone = get('input[name="phone"]') || get('input[name="mobile"]') || get('input[type="tel"]');
        const cleanPhone = normalizeIndianPhone(rawPhone);

        const name = get('input[name="user_name"]') || get('input[name="name"]') || get('input[name="full_name"]');
        const email = get('input[name="email"]') || get('input[type="email"]');
        
        let service = form.dataset.serviceId || 
                      get('select[name="category"]') || 
                      get('select[name="service"]') || 
                      get('input[name="service"]') || 
                      get('input[name="service_id"]') || 
                      document.title.split('|')[0].trim();

        const state = get('select[name="selected_state"]') || get('select[name="state"]');
        const message = get('textarea[name="custom_message"]') || get('textarea[name="message"]');

        return {
            name: name,
            phone: cleanPhone,
            raw_phone: rawPhone,
            email: email,
            service_requested: service,
            selected_state: state,
            custom_message: message,
            source_page: window.location.pathname,
            source_url: window.location.href,
            page_title: document.title,
            timestamp: new Date().toISOString(),
            user_agent: navigator.userAgent,
            utm_params: utm
        };
    }

    /**
     * Validates input values against strict Indian formats
     */
    function validate(data, form) {
        const errors = {};

        // 1. Name validation (Min 2 characters)
        if (!data.name || data.name.trim().length < 2) {
            errors.name = 'Please enter your full legal name (at least 2 characters).';
        }

        // 2. Mobile validation (Indian 10-digit starting with 6, 7, 8, or 9)
        const mobileRegex = /^[6-9]\d{9}$/;
        if (!data.phone || !mobileRegex.test(data.phone)) {
            errors.phone = 'Please enter a valid 10-digit Indian mobile number (e.g. 98765 43210).';
        }

        // 3. Email validation (only validate if field is present and filled or required)
        const emailField = _q(form, 'input[name="email"]') || _q(form, 'input[type="email"]');
        if (emailField) {
            const isRequired = emailField.hasAttribute('required');
            const emailVal = data.email || '';
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
            if ((isRequired && !emailVal) || (emailVal && !emailRegex.test(emailVal))) {
                errors.email = 'Please enter a valid business email address.';
            }
        }

        return {
            valid: Object.keys(errors).length === 0,
            errors
        };
    }

    /**
     * LocalStorage fail-safe backup for lead recovery
     */
    function saveLeadLocally(payload) {
        try {
            const cfg = _getConfig();
            const key = cfg.localStorageKey || 'ccs_lead_intakes';
            const stored = JSON.parse(localStorage.getItem(key) || '[]');
            stored.unshift(payload);
            if (stored.length > 50) stored.pop();
            localStorage.setItem(key, JSON.stringify(stored));
            console.log('[CCSForms] Lead successfully secured in localStorage.');
        } catch (e) {
            console.warn('[CCSForms] Local storage access error:', e);
        }
    }

    /**
     * Dispatches lead payload via fetch() to the webhook
     */
    async function dispatchLeadPayload(payload) {
        const cfg = _getConfig();
        const controller = new AbortController();
        const timeoutId = setTimeout(() => controller.abort(), cfg.webhookTimeoutMs || 6000);

        try {
            const response = await fetch(cfg.webhookUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-Craftegon-Source': 'WebClient-LeadEngine'
                },
                body: JSON.stringify(payload),
                signal: controller.signal
            });
            clearTimeout(timeoutId);
            return response;
        } catch (err) {
            clearTimeout(timeoutId);
            throw err;
        }
    }

    /**
     * Constructs a dynamic contextual WhatsApp URL
     */
    function getWhatsAppUrl(serviceName, price) {
        const cfg = _getConfig();
        const cleanName = serviceName ? serviceName.trim() : 'corporate compliance';
        let text = `Hi Craftegon, I want to apply for ${cleanName}`;
        if (price) {
            text += ` priced at ${price}`;
        }
        text += '. Please connect me with a CA/CS specialist.';
        return `https://wa.me/${cfg.whatsAppNumber}?text=${encodeURIComponent(text)}`;
    }

    /**
     * Inline success state with priority 10-minute promise
     */
    function renderSuccessState(form, payload) {
        const refId = 'CCS-' + Date.now().toString(36).toUpperCase();
        const serviceName = payload.service_requested || 'corporate advisory';
        const waFollowup = `https://wa.me/${_getConfig().whatsAppNumber}?text=${encodeURIComponent(`Hi Craftegon! I just submitted lead #${refId} for ${serviceName}. Connecting here for priority review.`)}`;

        const successHtml = `
            <div class="bg-white rounded-2xl p-6 sm:p-8 border border-emerald-200 shadow-xl text-center space-y-4 animate-fadeIn" role="status" aria-live="polite">
                <div class="w-14 h-14 bg-emerald-100 text-emerald-600 rounded-2xl flex items-center justify-center mx-auto text-2xl font-black shadow-sm">
                    ✓
                </div>
                <div>
                    <span class="text-[10px] font-bold uppercase tracking-wider text-emerald-700 bg-emerald-50 px-2.5 py-1 rounded-full">
                        Priority Callback Scheduled
                    </span>
                    <h3 class="text-xl font-extrabold text-brand-dark mt-2 mb-1">Thank You, ${payload.name}!</h3>
                    <p class="text-xs sm:text-sm text-slate-600 leading-relaxed max-w-sm mx-auto">
                        Your request for <strong>${serviceName}</strong> has been logged. An empaneled Craftegon CA/CS specialist will call you at <strong class="text-brand-dark">+91 ${payload.phone}</strong> within <strong>10 minutes</strong>.
                    </p>
                </div>
                <div class="p-3 bg-slate-50 rounded-xl border border-slate-200 text-xs font-mono text-slate-500">
                    Lead Ref ID: <span class="font-bold text-slate-800">${refId}</span>
                </div>
                <div class="pt-2">
                    <a href="${waFollowup}" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 bg-[#25D366] hover:bg-[#20bd5a] text-white text-xs font-bold px-5 py-3 rounded-xl shadow-md transition">
                        <span>💬 Need Faster Response? Chat on WhatsApp</span>
                    </a>
                </div>
            </div>
        `;

        form.outerHTML = successHtml;
    }

    /**
     * Unified Form Submit Handler
     */
    async function handleLeadSubmit(event) {
        event.preventDefault();
        const form = event.currentTarget || event.target;
        clearErrors(form);

        const payload = captureFields(form);
        const { valid, errors } = validate(payload, form);

        if (!valid) {
            // Highlight invalid fields
            Object.entries(errors).forEach(([fieldKey, message]) => {
                let field = null;
                if (fieldKey === 'name') {
                    field = _q(form, 'input[name="user_name"]') || _q(form, 'input[name="name"]') || _q(form, 'input[name="full_name"]');
                } else if (fieldKey === 'phone') {
                    field = _q(form, 'input[name="phone"]') || _q(form, 'input[name="mobile"]') || _q(form, 'input[type="tel"]');
                } else if (fieldKey === 'email') {
                    field = _q(form, 'input[name="email"]') || _q(form, 'input[type="email"]');
                }
                if (field) showFieldError(field, message);
            });

            const firstErr = form.querySelector('.border-rose-500');
            if (firstErr) firstErr.focus();
            return false;
        }

        // Set button loading state
        const submitBtn = form.querySelector('button[type="submit"]') || form.querySelector('input[type="submit"]');
        const origText = submitBtn ? submitBtn.innerHTML : 'Submit';
        if (submitBtn) {
            submitBtn.disabled = true;
            submitBtn.innerHTML = `
                <span class="inline-flex items-center gap-2">
                    <svg class="animate-spin h-4 w-4 text-white" viewBox="0 0 24 24" fill="none"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v8H4z"></path></svg>
                    <span>Routing to Legal Desk...</span>
                </span>
            `;
        }

        // 1. Fail-safe local backup
        saveLeadLocally(payload);

        // 2. Dispatch to Webhook / API
        try {
            await dispatchLeadPayload(payload);
            console.log('[CCSForms] Webhook received lead payload successfully.');
        } catch (err) {
            console.warn('[CCSForms] Webhook dispatch bypassed or offline, lead safely persisted locally.', err);
        }

        // 3. Render clean conversion confirmation state
        setTimeout(() => {
            renderSuccessState(form, payload);
        }, 400);

        return true;
    }

    /**
     * Auto-populates service dropdowns based on page route
     */
    function autoPopulateServiceSelector() {
        const path = window.location.pathname.toLowerCase();
        let targetCategory = '';

        if (path.includes('gst')) targetCategory = 'gst-advisory';
        else if (path.includes('pvt-ltd') || path.includes('business-setup') || path.includes('llp') || path.includes('opc')) targetCategory = 'business-setup';
        else if (path.includes('trademark') || path.includes('brand-protection')) targetCategory = 'brand-protection';
        else if (path.includes('corporate-governance')) targetCategory = 'corporate-governance';
        else if (path.includes('direct-tax') || path.includes('tax')) targetCategory = 'direct-tax';
        else if (path.includes('workforce-digital')) targetCategory = 'workforce-digital';

        if (!targetCategory) return;

        document.querySelectorAll('select[name="category"]').forEach(select => {
            for (let i = 0; i < select.options.length; i++) {
                if (select.options[i].value === targetCategory) {
                    select.selectedIndex = i;
                    break;
                }
            }
        });
    }

    /**
     * Upgrades all WhatsApp buttons to contextual prefilled URLs
     */
    function enhanceWhatsAppButtons() {
        // 1. Explicit data attributes
        document.querySelectorAll('[data-wa-service]').forEach(btn => {
            const service = btn.dataset.waService || '';
            const price = btn.dataset.waPrice || '';
            btn.href = getWhatsAppUrl(service, price);
        });

        // 2. Dynamic card inference for any service cards & pricing tables
        document.querySelectorAll('a[href*="wa.me/918606918247"]').forEach(btn => {
            if (btn.id === 'ccs-mobile-sticky-bar' || btn.closest('#ccs-mobile-sticky-bar') || btn.closest('#ccs-desktop-floating-cta')) {
                return;
            }
            const card = btn.closest('.group, [data-service-card], .rounded-2xl, .rounded-3xl, .bg-white');
            if (card) {
                const heading = card.querySelector('h2, h3, h4');
                const priceEl = card.querySelector('.font-black, .font-extrabold, .text-2xl, .text-3xl');
                if (heading) {
                    const sName = heading.textContent.trim();
                    const sPrice = priceEl ? priceEl.textContent.trim().replace('+ State Stamp Duty', '').replace('+ GST', '').replace('+ statutory fee', '').trim() : '';
                    if (sName && sName.length > 2 && !btn.href.includes(encodeURIComponent(sName))) {
                        btn.href = getWhatsAppUrl(sName, sPrice);
                    }
                }
            }
        });
    }

    /**
     * Populates state selects
     */
    function populateStateSelects() {
        document.querySelectorAll('select[name="selected_state"], select[name="state"]').forEach(select => {
            if (select.options.length > 2) return;
            INDIAN_STATES.forEach(st => {
                const opt = document.createElement('option');
                opt.value = st;
                opt.textContent = st;
                select.appendChild(opt);
            });
        });
    }

    /**
     * Initializer
     */
    function init() {
        autoPopulateServiceSelector();
        populateStateSelects();
        enhanceWhatsAppButtons();

        // Bind all CCS forms and standard lead forms
        const forms = document.querySelectorAll('form[data-ccs-form], form#heroForm, form#contactForm, form#sidebarForm, form#knowledgeSidebarForm');
        forms.forEach(f => {
            f.removeEventListener('submit', handleLeadSubmit);
            f.addEventListener('submit', handleLeadSubmit);

            // Real-time error dismissal on input
            f.querySelectorAll('input, select, textarea').forEach(input => {
                input.addEventListener('input', () => {
                    input.classList.remove('border-rose-500', 'focus:ring-rose-500', 'bg-rose-50/50');
                    input.classList.add('border-slate-200');
                    const err = input.parentElement.querySelector('.ccs-form-error');
                    if (err) err.remove();
                });
            });
        });

        console.log(`[CCSForms] Conversion Engine active across ${forms.length} forms.`);
    }

    return {
        init,
        handleLeadSubmit,
        captureFields,
        validate,
        normalizeIndianPhone,
        dispatchLeadPayload,
        saveLeadLocally,
        getWhatsAppUrl,
        renderSuccessState,
        INDIAN_STATES
    };
})();

// Global exposure
if (typeof window !== 'undefined') {
    window.CCSForms = CCSForms;
    window.handleHeroSubmit = function (e) {
        return CCSForms.handleLeadSubmit(e);
    };
    window.handleSidebarSubmit = function (e) {
        return CCSForms.handleLeadSubmit(e);
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', CCSForms.init);
    } else {
        CCSForms.init();
    }
}
