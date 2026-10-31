/**
 * CraftEgon Corporate Services — Form Handler Engine
 * ====================================================
 * Centralizes all form submissions across the platform.
 *
 * Features:
 *  - Auto-discovery of [data-ccs-form] forms
 *  - Client-side validation (name, email, phone)
 *  - POST to /api/lead-capture with 8s timeout
 *  - WhatsApp fallback with pre-filled message
 *  - UTM param capture
 *  - Indian state <select> population
 *
 * @module CCSForms
 * @version 1.0.0
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

/* ── WhatsApp Contact ─────────────────────────────────────── */
const CCS_WHATSAPP_NUMBER = '918606918247';

/* ============================================================
   CCSForms Namespace
   ============================================================ */
const CCSForms = (function () {

  /* ── Internal Helpers ─────────────────────────────────────── */

  /**
   * Reads UTM parameters and returns them as a flat object.
   * @returns {{ utm_source: string, utm_medium: string, utm_campaign: string }}
   */
  function _getUtmParams() {
    const params = new URLSearchParams(window.location.search);
    return {
      utm_source:   params.get('utm_source')   || '',
      utm_medium:   params.get('utm_medium')   || '',
      utm_campaign: params.get('utm_campaign') || '',
    };
  }

  /**
   * Returns the current ISO timestamp.
   * @returns {string}
   */
  function _timestamp() {
    return new Date().toISOString();
  }

  /**
   * Safe query helper — returns null without throwing.
   * @param {HTMLElement} form
   * @param {string} selector
   * @returns {HTMLElement|null}
   */
  function _q(form, selector) {
    try { return form.querySelector(selector); } catch { return null; }
  }

  /**
   * Adds the CSS error class + inserts a form-error <p>.
   * @param {HTMLElement} field
   * @param {string} message
   */
  function showFieldError(field, message) {
    if (!field) return;
    field.classList.add('has-error');

    // Remove any existing error node for this field
    const prev = field.parentElement.querySelector('.form-error[data-for="' + field.name + '"]');
    if (prev) prev.remove();

    const err = document.createElement('p');
    err.className = 'form-error';
    err.dataset.for = field.name || '';
    err.setAttribute('role', 'alert');
    err.innerHTML = `<span aria-hidden="true">⚠</span> ${message}`;
    field.parentElement.appendChild(err);
  }

  /**
   * Clears all error states inside a form.
   * @param {HTMLElement} form
   */
  function clearErrors(form) {
    form.querySelectorAll('.has-error').forEach(el => el.classList.remove('has-error'));
    form.querySelectorAll('.form-error[data-for]').forEach(el => el.remove());
  }

  /* ── captureFields ────────────────────────────────────────── */

  /**
   * Extracts all relevant fields from the form element.
   * @param {HTMLFormElement} form
   * @returns {Object} Flat payload object ready for submission.
   */
  function captureFields(form) {
    const utm = _getUtmParams();

    const get = selector => {
      const el = _q(form, selector);
      return el ? el.value.trim() : '';
    };

    return {
      // Service metadata (from form attributes or hidden inputs)
      service_id:      form.dataset.serviceId      || get('input[name="service_id"]')       || '',
      category:        form.dataset.category       || get('input[name="category"]')          || '',

      // User-submitted fields
      user_name:       get('input[name="user_name"]'),
      email:           get('input[name="email"]'),
      phone:           get('input[name="phone"]'),
      selected_state:  get('select[name="selected_state"]'),
      custom_message:  get('textarea[name="custom_message"]'),

      // Tracking
      timestamp:       _timestamp(),
      page_url:        window.location.href,
      utm_source:      utm.utm_source,
      utm_medium:      utm.utm_medium,
      utm_campaign:    utm.utm_campaign,
    };
  }

  /* ── validate ─────────────────────────────────────────────── */

  /**
   * Validates the captured payload object.
   * @param {Object} data  Output of captureFields()
   * @returns {{ valid: boolean, errors: Object }}
   */
  function validate(data) {
    const errors = {};

    // Name — minimum 2 meaningful characters
    if (!data.user_name || data.user_name.length < 2) {
      errors.user_name = 'Please enter your full name (at least 2 characters).';
    }

    // Email — RFC-5322 simplified regex
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    if (!data.email || !emailRegex.test(data.email)) {
      errors.email = 'Please enter a valid email address.';
    }

    // Phone — Indian mobile: 10 digits, starts with 6–9
    if (data.phone) {
      const digits = data.phone.replace(/\D/g, '');
      const mobileRegex = /^[6-9]\d{9}$/;
      if (!mobileRegex.test(digits)) {
        errors.phone = 'Enter a valid 10-digit Indian mobile number starting with 6–9.';
      }
    }
    // Phone is optional — only validate if provided
    // (remove the `if (data.phone)` wrapper above to make it required)

    return {
      valid:  Object.keys(errors).length === 0,
      errors,
    };
  }

  /* ── submitToBackend ──────────────────────────────────────── */

  /**
   * POSTs JSON data to /api/lead-capture with an 8-second timeout.
   * @param {Object} data
   * @returns {Promise<Response>}
   */
  async function submitToBackend(data) {
    const controller = new AbortController();
    const timeoutId  = setTimeout(() => controller.abort(), 8000);

    try {
      const response = await fetch('/api/lead-capture', {
        method:  'POST',
        headers: { 'Content-Type': 'application/json' },
        body:    JSON.stringify(data),
        signal:  controller.signal,
      });
      clearTimeout(timeoutId);
      return response;
    } catch (err) {
      clearTimeout(timeoutId);
      throw err; // Re-throw so handleSubmit can catch it
    }
  }

  /* ── generateWhatsAppLink ─────────────────────────────────── */

  /**
   * Generates a pre-filled WhatsApp link for CraftEgon's number.
   * @param {Object} data  Output of captureFields()
   * @returns {string}  Full WhatsApp URL
   */
  function generateWhatsAppLink(data) {
    const service = data.service_id || 'your service';
    const name    = data.user_name  || 'N/A';
    const email   = data.email      || 'N/A';
    const state   = data.selected_state || 'N/A';
    const msg     = data.custom_message ? ` Additional info: ${data.custom_message}` : '';

    const template =
      `Hi CraftEgon! I need help with ${service}. ` +
      `Name: ${name}, Email: ${email}, State: ${state}.${msg}`;

    const encoded = encodeURIComponent(template);
    return `https://wa.me/${CCS_WHATSAPP_NUMBER}?text=${encoded}`;
  }

  /* ── showSuccess ──────────────────────────────────────────── */

  /**
   * Replaces the form HTML with a branded success card.
   * @param {HTMLFormElement} form
   * @param {string} [serviceTitle]
   */
  function showSuccess(form, serviceTitle) {
    const title = serviceTitle || 'your request';
    const html = `
      <div class="success-card" role="status" aria-live="polite">
        <div class="success-icon">✅</div>
        <h3>Thank you!</h3>
        <p>
          We've received your enquiry for <strong>${title}</strong>.<br>
          Our team will reach out within <strong>1 business day</strong>.
        </p>
        <p class="text-xs text-muted mt-4">
          Reference: CCS-${Date.now().toString(36).toUpperCase()}
        </p>
      </div>
    `;
    form.outerHTML = html;
  }

  /* ── showWhatsAppFallback ─────────────────────────────────── */

  /**
   * Inserts a WhatsApp fallback CTA after the form when the backend is unreachable.
   * @param {HTMLFormElement} form
   * @param {string} waLink
   */
  function showWhatsAppFallback(form, waLink) {
    const html = `
      <div class="whatsapp-fallback-card" role="alert">
        <p class="font-semibold mb-4">
          ⚠️ We couldn't submit your form right now — no worries!
        </p>
        <p class="text-sm mb-6">
          Connect with us directly on WhatsApp — your details are pre-filled.
        </p>
        <a
          href="${waLink}"
          target="_blank"
          rel="noopener noreferrer"
          class="btn btn-whatsapp"
          aria-label="Chat with CraftEgon on WhatsApp"
        >
          <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">
            <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>
          </svg>
          Chat on WhatsApp
        </a>
      </div>
    `;

    // Insert fallback after form; keep form accessible for retry
    const wrapper = document.createElement('div');
    wrapper.innerHTML = html;
    form.insertAdjacentElement('afterend', wrapper.firstElementChild);

    // Hide the original form but keep its DOM for potential retry
    form.style.display = 'none';
  }

  /* ── handleSubmit ─────────────────────────────────────────── */

  /**
   * Main form submission handler. Bound to each [data-ccs-form] element.
   * @param {SubmitEvent} event
   */
  async function handleSubmit(event) {
    event.preventDefault();
    const form = event.currentTarget;

    clearErrors(form);

    // Capture fields
    const data = captureFields(form);
    console.log('[CCSForms] Captured fields:', data);

    // Validate
    const { valid, errors } = validate(data);

    if (!valid) {
      console.warn('[CCSForms] Validation failed:', errors);

      // Highlight each invalid field
      Object.entries(errors).forEach(([fieldName, message]) => {
        const field =
          _q(form, `input[name="${fieldName}"]`) ||
          _q(form, `select[name="${fieldName}"]`) ||
          _q(form, `textarea[name="${fieldName}"]`);
        showFieldError(field, message);
      });

      // Focus first error field
      const firstError = form.querySelector('.has-error');
      if (firstError) firstError.focus();
      return;
    }

    // Set loading state
    const submitBtn = form.querySelector('[type="submit"]');
    const originalLabel = submitBtn ? submitBtn.textContent : '';
    if (submitBtn) {
      submitBtn.disabled = true;
      submitBtn.classList.add('is-loading');
      submitBtn.textContent = 'Submitting…';
    }

    // Generate WhatsApp link upfront (needed for fallback)
    const waLink = generateWhatsAppLink(data);

    try {
      const response = await submitToBackend(data);

      if (response.ok) {
        console.log('[CCSForms] Submission successful:', response.status);
        const serviceTitle = form.dataset.serviceTitle || data.service_id || 'your request';
        showSuccess(form, serviceTitle);
      } else {
        // Server responded but with an error code
        const errBody = await response.text().catch(() => '');
        console.error('[CCSForms] Server error:', response.status, errBody);
        showWhatsAppFallback(form, waLink);
      }
    } catch (err) {
      // Network error or timeout (AbortError)
      if (err.name === 'AbortError') {
        console.warn('[CCSForms] Request timed out — showing WhatsApp fallback.');
      } else {
        console.error('[CCSForms] Network error:', err);
      }
      showWhatsAppFallback(form, waLink);
    } finally {
      // Restore button if form is still in DOM
      if (submitBtn && document.body.contains(submitBtn)) {
        submitBtn.disabled = false;
        submitBtn.classList.remove('is-loading');
        submitBtn.textContent = originalLabel;
      }
    }
  }

  /* ── populateStateSelects ─────────────────────────────────── */

  /**
   * Populates every <select name="selected_state"> in the document
   * with the full INDIAN_STATES list.
   */
  function populateStateSelects() {
    const selects = document.querySelectorAll('select[name="selected_state"]');
    selects.forEach(select => {
      // Preserve any existing placeholder option
      const placeholder = select.querySelector('option[value=""]');
      select.innerHTML = '';

      if (placeholder) {
        select.appendChild(placeholder);
      } else {
        const ph = document.createElement('option');
        ph.value = '';
        ph.textContent = 'Select your state';
        ph.disabled = true;
        ph.selected = true;
        select.appendChild(ph);
      }

      INDIAN_STATES.forEach(state => {
        const opt = document.createElement('option');
        opt.value = state;
        opt.textContent = state;
        select.appendChild(opt);
      });
    });
  }

  /* ── init ─────────────────────────────────────────────────── */

  /**
   * Auto-discovers all [data-ccs-form] elements and attaches handlers.
   * Called on DOMContentLoaded.
   */
  function init() {
    populateStateSelects();

    const forms = document.querySelectorAll('[data-ccs-form]');
    console.log(`[CCSForms] Initialised — found ${forms.length} form(s).`);

    forms.forEach(form => {
      form.addEventListener('submit', handleSubmit);

      // Live validation — clear error on input
      form.querySelectorAll('input, select, textarea').forEach(field => {
        field.addEventListener('input', () => {
          field.classList.remove('has-error');
          const err = field.parentElement.querySelector(`.form-error[data-for="${field.name}"]`);
          if (err) err.remove();
        });
      });
    });
  }

  /* ── Public API ───────────────────────────────────────────── */
  return {
    init,
    captureFields,
    validate,
    showFieldError,
    clearErrors,
    submitToBackend,
    generateWhatsAppLink,
    handleSubmit,
    showSuccess,
    showWhatsAppFallback,
    populateStateSelects,
    INDIAN_STATES,
  };

})();

/* ── Auto-init on DOM ready ───────────────────────────────── */
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', CCSForms.init);
} else {
  CCSForms.init();
}
