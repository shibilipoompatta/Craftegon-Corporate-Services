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
});

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
