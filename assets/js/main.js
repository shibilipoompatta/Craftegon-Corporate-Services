/**
 * CraftEgon Corporate Services — Main Application Logic & Search Engine
 * ====================================================================
 * Fast real-time client-side search across 150+ legal & tax services,
 * category filtering, mobile navigation, and lead intake handling.
 *
 * @version 2.0.0
 */

'use strict';

// Global services store for instant client-side lookup (<50ms)
let craftegonServices = [];
let activeSearchCategory = 'all';
let searchDebounceTimer = null;

document.addEventListener('DOMContentLoaded', () => {
    initLeadForms();
    initMobileNav();
    initGlobalSearchEngine();
    initFloatingCTAs();
});

/**
 * High-Converting Mobile Sticky CTA Bar & Desktop Floating WhatsApp Widget
 */
function initFloatingCTAs() {
    if (document.getElementById('ccs-mobile-sticky-bar')) return;

    // Determine current service name for contextual WhatsApp prefill
    let pageContext = 'corporate compliance';
    const path = window.location.pathname.toLowerCase();
    if (path.includes('gst')) pageContext = 'GST Registration & Filings';
    else if (path.includes('pvt-ltd') || path.includes('business-setup')) pageContext = 'Private Limited & Business Setup';
    else if (path.includes('trademark') || path.includes('brand-protection')) pageContext = 'Trademark & Brand Protection';
    else if (path.includes('corporate-governance')) pageContext = 'Annual MCA & ROC Compliance';
    else if (path.includes('direct-tax')) pageContext = 'Direct Tax & TDS Advisory';
    else if (path.includes('workforce-digital')) pageContext = 'Workforce & DPDP Compliance';
    else if (path.includes('licenses')) pageContext = 'Trade Licenses & Certifications';

    const waText = encodeURIComponent(`Hi Craftegon, I need assistance with ${pageContext}.`);
    const waUrl = `https://wa.me/918606918247?text=${waText}`;

    // 1. Mobile Sticky Bottom Bar (<768px)
    const mobileBar = document.createElement('div');
    mobileBar.id = 'ccs-mobile-sticky-bar';
    mobileBar.className = 'md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center gap-3 shadow-2xl safe-area-bottom';
    mobileBar.innerHTML = `
        <a href="tel:+918606918247" class="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold text-xs py-3 px-3 rounded-xl border border-slate-200 flex items-center justify-center gap-2 transition min-touch">
            <svg class="w-4 h-4 text-brand-sky" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>Talk to CA/CS</span>
        </a>
        <a href="${waUrl}" target="_blank" rel="noopener noreferrer" class="flex-1 bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs py-3 px-3 rounded-xl shadow-md flex items-center justify-center gap-2 transition min-touch">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            <span>Instant WhatsApp</span>
        </a>
    `;

    // 2. Desktop/Tablet Floating WhatsApp Widget (>=768px)
    const desktopWidget = document.createElement('aside');
    desktopWidget.id = 'ccs-desktop-floating-cta';
    desktopWidget.setAttribute('aria-label', 'WhatsApp Consultation Support');
    desktopWidget.className = 'hidden md:block fixed bottom-6 right-6 z-40';
    desktopWidget.innerHTML = `
        <a href="${waUrl}" target="_blank" rel="noopener noreferrer" aria-label="Chat with CA/CS on WhatsApp" class="flex items-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-4 py-3 rounded-full shadow-2xl hover:shadow-emerald-500/30 transition-all duration-300 hover:scale-105 group">
            <span class="relative flex h-3 w-3">
                <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-white opacity-75"></span>
                <span class="relative inline-flex rounded-full h-3 w-3 bg-white"></span>
            </span>
            <svg class="w-6 h-6 fill-current shrink-0" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            <div class="text-left font-sans">
                <span class="block text-[10px] text-emerald-100 uppercase tracking-wider font-semibold">Verified Online</span>
                <span class="block text-xs font-bold leading-tight">Chat with CA/CS</span>
            </div>
        </a>
    </aside>
    `;

    document.body.appendChild(mobileBar);
    document.body.appendChild(desktopWidget);

    // Add bottom padding on mobile so content isn't obscured
    document.body.classList.add('pb-16', 'md:pb-0');
}

/**
 * Lead Capture & Consultation Form Submission Handler
 */
function initLeadForms() {
    const forms = document.querySelectorAll('form:not([role="search"]):not(#searchForm)');
    
    forms.forEach(form => {
        // Skip forms that already have specialized handlers
        if (form.hasAttribute('data-ccs-form') || form.hasAttribute('onsubmit')) {
            return;
        }

        form.addEventListener('submit', (e) => {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const originalBtnText = submitBtn ? submitBtn.innerHTML : 'Submit';

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = `<span>Processing Request...</span>`;
            }

            // Simulate server submission API call
            setTimeout(() => {
                alert('Thank you! Your request has been received. A Craftegon specialist will contact you shortly.');
                form.reset();
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalBtnText;
                }
            }, 800);
        });
    });
}

/**
 * Mobile Navigation Drawer Toggle Handler
 */
function initMobileNav() {
    const toggleBtn = document.getElementById('mobile-menu-toggle') || document.getElementById('mobileMenuBtn');
    const mobileMenu = document.getElementById('mobile-menu') || document.getElementById('mobileMenu');

    if (toggleBtn && mobileMenu) {
        toggleBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            mobileMenu.classList.toggle('hidden');
        });
    }
}

/**
 * Fast Real-Time Client-Side Search Engine
 */
async function initGlobalSearchEngine() {
    const searchInput = document.getElementById('searchInput') || document.getElementById('serviceSearchInput');
    const resultsContainer = document.getElementById('searchResultsDropdown');
    const searchForm = document.getElementById('searchForm');
    const categoryChips = document.querySelectorAll('.search-chip');

    // 1. Asynchronously prefetch services catalog
    try {
        const endpoints = [
            '/data/craftegon-services.json',
            'data/craftegon-services.json',
            '/data/services.json'
        ];
        for (const ep of endpoints) {
            try {
                const res = await fetch(ep);
                if (res.ok) {
                    const data = await res.json();
                    craftegonServices = data.services || [];
                    if (craftegonServices.length > 0) break;
                }
            } catch (err) {
                // Try next endpoint
            }
        }
    } catch (e) {
        console.warn('[SearchEngine] Could not load remote catalog:', e);
    }

    if (!searchInput) return;

    // 2. Bind Category Filter Chips
    if (categoryChips.length > 0) {
        categoryChips.forEach(chip => {
            chip.addEventListener('click', () => {
                categoryChips.forEach(c => {
                    c.classList.remove('bg-brand-sky', 'text-white', 'shadow-xs');
                    c.classList.add('bg-slate-100', 'text-slate-700');
                });
                chip.classList.remove('bg-slate-100', 'text-slate-700');
                chip.classList.add('bg-brand-sky', 'text-white', 'shadow-xs');

                activeSearchCategory = chip.dataset.cat || 'all';
                filterAndRenderResults(searchInput.value.trim());
            });
        });
    }

    // 3. Debounced Real-Time Input Handler (<50ms response)
    searchInput.addEventListener('input', (e) => {
        clearTimeout(searchDebounceTimer);
        searchDebounceTimer = setTimeout(() => {
            filterAndRenderResults(e.target.value.trim());
        }, 40);
    });

    searchInput.addEventListener('focus', () => {
        if (searchInput.value.trim().length >= 1 || activeSearchCategory !== 'all') {
            filterAndRenderResults(searchInput.value.trim());
        }
    });

    // 4. Click-outside listener to dismiss results
    document.addEventListener('click', (e) => {
        const searchBox = document.getElementById('searchContainer');
        if (searchBox && !searchBox.contains(e.target) && resultsContainer) {
            resultsContainer.classList.add('hidden');
        }
    });

    // 5. Escape key to dismiss
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && resultsContainer) {
            resultsContainer.classList.add('hidden');
        }
    });
}

/**
 * Filter services and render high-converting result cards
 */
function filterAndRenderResults(query) {
    const resultsContainer = document.getElementById('searchResultsDropdown');
    if (!resultsContainer) return;

    if (!query && activeSearchCategory === 'all') {
        resultsContainer.classList.add('hidden');
        resultsContainer.innerHTML = '';
        return;
    }

    const q = query.toLowerCase();
    const queryTokens = q.split(/\s+/).filter(t => t.length > 0);

    const matches = craftegonServices.filter(s => {
        // Category constraint
        if (activeSearchCategory !== 'all') {
            if (activeSearchCategory === 'licenses') {
                const isLicense = s.title.toLowerCase().includes('license') || 
                                  s.title.toLowerCase().includes('fssai') || 
                                  s.title.toLowerCase().includes('udyam') ||
                                  s.title.toLowerCase().includes('iec');
                if (!isLicense) return false;
            } else if (s.category !== activeSearchCategory) {
                return false;
            }
        }

        if (queryTokens.length === 0) return true;

        const title = (s.title || '').toLowerCase();
        const desc = (s.short_description || '').toLowerCase();
        const cat = (s.category || '').toLowerCase();
        const kws = Array.isArray(s.keywords) ? s.keywords.join(' ').toLowerCase() : '';

        // Match all tokens or at least main token
        return queryTokens.some(token => 
            title.includes(token) || 
            desc.includes(token) || 
            cat.includes(token) ||
            kws.includes(token)
        );
    });

    // Render results
    if (matches.length === 0) {
        resultsContainer.innerHTML = `
            <div class="p-6 text-center">
                <div class="w-12 h-12 rounded-2xl bg-amber-50 text-amber-600 flex items-center justify-center mx-auto mb-3 text-xl font-bold">
                    🔍
                </div>
                <h4 class="text-sm font-bold text-brand-dark mb-1">No matching service found for "${escapeHtml(query)}"</h4>
                <p class="text-xs text-slate-500 mb-4 max-w-xs mx-auto">
                    We cover 150+ legal, tax, and compliance services. Request a 10-minute CA callback for custom assistance.
                </p>
                <div class="flex items-center justify-center gap-3">
                    <a href="#contact" onclick="document.getElementById('searchResultsDropdown').classList.add('hidden')" class="bg-brand-sky hover:bg-brand-skyHover text-white text-xs font-bold px-4 py-2 rounded-xl transition shadow-sm">
                        Request 10-Min Callback &rarr;
                    </a>
                    <a href="https://wa.me/918606918247?text=${encodeURIComponent('Hi CraftEgon! I was looking for ' + query + ' on your platform.')}" target="_blank" rel="noopener noreferrer" class="bg-[#25D366] text-white text-xs font-bold px-4 py-2 rounded-xl transition">
                        Ask on WhatsApp 💬
                    </a>
                </div>
            </div>
        `;
        resultsContainer.classList.remove('hidden');
        return;
    }

    const categoryNames = {
        'business-setup': 'Business Setup',
        'gst-advisory': 'GST & Tax',
        'corporate-governance': 'Corporate MCA',
        'direct-tax': 'Direct Tax',
        'brand-protection': 'Trademark & IP',
        'workforce-digital': 'Workforce'
    };

    const cardsHtml = matches.slice(0, 7).map(s => {
        const catLabel = categoryNames[s.category] || s.category;
        const price = s.starting_price ? `₹${s.starting_price.toLocaleString('en-IN')}` : 'Starting @ ₹999';
        const timeline = s.timeline_days || '3-5 Days';
        const link = s.product_path || s.hub_path || '/business-setup/';
        const guideLink = `/knowledge/${s.slug}-guide.html`;
        const waLink = `https://wa.me/918606918247?text=${encodeURIComponent('Hi CraftEgon! I want to apply for ' + s.title + ' (' + price + ').')}`;

        return `
            <div class="flex items-center justify-between p-3.5 hover:bg-slate-50 transition group">
                <div class="flex items-center gap-3 pr-2 min-w-0">
                    <div class="w-9 h-9 rounded-xl bg-brand-skyLight text-brand-sky flex items-center justify-center font-bold text-xs shrink-0 group-hover:bg-brand-sky group-hover:text-white transition">
                        📄
                    </div>
                    <div class="min-w-0">
                        <a href="${link}" class="text-xs sm:text-sm font-bold text-brand-dark group-hover:text-brand-sky transition truncate block">
                            ${escapeHtml(s.title)}
                        </a>
                        <div class="text-[10px] text-slate-500 flex items-center gap-2 mt-0.5">
                            <span class="px-2 py-0.5 rounded-md bg-slate-100 font-semibold text-slate-600">${escapeHtml(catLabel)}</span>
                            <span>·</span>
                            <span class="text-slate-500">⏱️ ${escapeHtml(timeline)}</span>
                        </div>
                    </div>
                </div>
                <div class="text-right shrink-0 flex items-center gap-3">
                    <div class="hidden sm:block text-right">
                        <span class="text-xs sm:text-sm font-black text-brand-dark block">${price}</span>
                        <span class="text-[9px] text-slate-400 block">+ statutory fee</span>
                    </div>
                    <a href="${waLink}" target="_blank" rel="noopener noreferrer" class="bg-brand-sky hover:bg-brand-skyHover text-white text-xs font-bold px-3 py-1.5 rounded-lg shadow-xs transition whitespace-nowrap">
                        Apply Now
                    </a>
                </div>
            </div>
        `;
    }).join('');

    resultsContainer.innerHTML = cardsHtml;
    resultsContainer.classList.remove('hidden');
}

/**
 * Form submit handler for the search bar
 */
function handleQuickSearch(e) {
    if (e) e.preventDefault();
    const searchInput = document.getElementById('searchInput') || document.getElementById('serviceSearchInput');
    if (!searchInput) return;

    const q = searchInput.value.toLowerCase().trim();
    if (!q) {
        if (activeSearchCategory !== 'all') {
            window.location.href = `/${activeSearchCategory}/`;
        }
        return;
    }

    // Direct match against loaded catalog
    if (craftegonServices.length > 0) {
        const exact = craftegonServices.find(s => s.title.toLowerCase() === q || s.slug === q);
        if (exact) {
            window.location.href = exact.product_path || exact.hub_path;
            return;
        }
        const partial = craftegonServices.find(s => s.title.toLowerCase().includes(q));
        if (partial) {
            window.location.href = partial.product_path || partial.hub_path;
            return;
        }
    }

    // Category fallbacks
    if (q.includes('gst')) window.location.href = '/gst-advisory/';
    else if (q.includes('trade') || q.includes('ip') || q.includes('brand') || q.includes('logo')) window.location.href = '/brand-protection/';
    else if (q.includes('mca') || q.includes('roc') || q.includes('director')) window.location.href = '/corporate-governance/';
    else if (q.includes('tax') || q.includes('tds') || q.includes('itr')) window.location.href = '/direct-tax/';
    else if (q.includes('dpdp') || q.includes('posh') || q.includes('hr')) window.location.href = '/workforce-digital/';
    else window.location.href = '/business-setup/';
}

function escapeHtml(str) {
    return String(str || '').replace(/[&<>'"]/g, tag => ({
        '&': '&amp;',
        '<': '&lt;',
        '>': '&gt;',
        "'": '&#39;',
        '"': '&quot;'
    }[tag] || tag));
}

// Expose handleQuickSearch globally
window.handleQuickSearch = handleQuickSearch;
