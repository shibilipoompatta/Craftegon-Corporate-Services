/**
 * CraftEgon Corporate Services — Native Knowledge Hub Engine
 * ==========================================================
 * Route-based dynamic guide and FAQ injector for Craftegon Corporate Services.
 * Fetches data/craftegon-knowledge-hub.json and auto-injects targeted compliance
 * manuals and interactive FAQ accordions based on page context.
 *
 * @version 2.0.0
 */

'use strict';

const CraftegonKnowledgeHub = (function () {
    let _cachedGuides = null;

    /**
     * Category / route keyword routing map
     */
    const ROUTE_CATEGORY_MAP = {
        'pvt-ltd': 'business-setup',
        'business-setup': 'business-setup',
        'gst': 'gst-advisory',
        'gst-advisory': 'gst-advisory',
        'trademark': 'brand-protection',
        'brand-protection': 'brand-protection',
        'licenses': 'business-setup',
        'corporate-governance': 'corporate-governance',
        'direct-tax': 'direct-tax',
        'workforce-digital': 'workforce-digital'
    };

    /**
     * Fallback guides when offline or network fails
     */
    const FALLBACK_GUIDES = [
        {
            guide_id: "pvt-ltd-incorporation-guide",
            title: "Private Limited Company Incorporation: Complete Legal Manual",
            slug: "pvt-ltd-incorporation-guide",
            category: "business-setup",
            meta_description: "Step-by-step procedure under Companies Act 2013 and SPICe+ MCA V3 portal with document checklists and stamp duties.",
            read_time: "7 min read"
        },
        {
            guide_id: "gst-registration-guide",
            title: "GST Registration in India: Thresholds, Verification & Application",
            slug: "gst-registration-guide",
            category: "gst-advisory",
            meta_description: "Turnover limits, Aadhaar authentication, documents required, and input tax credit rules under CGST Act 2017.",
            read_time: "6 min read"
        },
        {
            guide_id: "trademark-registration-guide",
            title: "Trademark Registration in India: Nice Classification & Search",
            slug: "trademark-registration-guide",
            category: "brand-protection",
            meta_description: "Form TM-A filing, public trademark search, handling examination reports, and journal publication under Trade Marks Act 1999.",
            read_time: "7 min read"
        },
        {
            guide_id: "annual-roc-filing-guide",
            title: "Annual MCA ROC Compliance: AOC-4, MGT-7 & DIR-3 KYC Manual",
            slug: "annual-roc-filing-guide",
            category: "corporate-governance",
            meta_description: "Statutory audit requirements, board reports, AGM resolutions, and filing forms AOC-4 & MGT-7 under Companies Act 2013.",
            read_time: "7 min read"
        }
    ];

    /**
     * Fetch knowledge data asynchronously
     */
    async function fetchGuides() {
        if (_cachedGuides) return _cachedGuides;

        const endpoints = [
            '/data/craftegon-knowledge-hub.json',
            'data/craftegon-knowledge-hub.json',
            '../data/craftegon-knowledge-hub.json'
        ];

        for (const ep of endpoints) {
            try {
                const res = await fetch(ep);
                if (res.ok) {
                    const data = await res.json();
                    if (data && data.guides && data.guides.length > 0) {
                        _cachedGuides = data.guides;
                        return _cachedGuides;
                    }
                }
            } catch (e) {
                // Try next relative endpoint
            }
        }

        console.warn('[CraftegonKnowledgeHub] Using offline fallback guides.');
        _cachedGuides = FALLBACK_GUIDES;
        return _cachedGuides;
    }

    /**
     * Detect category from current URL or container context
     */
    function detectCurrentCategory() {
        const path = window.location.pathname.toLowerCase();
        for (const [key, cat] of Object.entries(ROUTE_CATEGORY_MAP)) {
            if (path.includes(key)) {
                return cat;
            }
        }
        return 'all';
    }

    /**
     * Render guide cards into a target container
     */
    function renderCards(container, guides) {
        if (!container) return;

        if (!guides || guides.length === 0) {
            container.innerHTML = `
                <div class="col-span-full text-center py-8 text-slate-400 text-sm">
                    No legal manuals found for this category.
                </div>
            `;
            return;
        }

        const categoryBadges = {
            'business-setup': 'Business Setup',
            'gst-advisory': 'GST & Tax',
            'brand-protection': 'Trademark & IP',
            'corporate-governance': 'MCA & ROC',
            'direct-tax': 'Direct Tax',
            'workforce-digital': 'Workforce Compliance'
        };

        container.innerHTML = guides.map(g => {
            const badge = categoryBadges[g.category] || 'Legal Manual';
            const link = `/knowledge/${g.slug}.html`;
            const waLink = `https://wa.me/918606918247?text=${encodeURIComponent('Hi CraftEgon! I have a question regarding ' + g.title + '.')}`;

            return `
                <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between group">
                    <div>
                        <div class="flex items-center justify-between mb-3">
                            <span class="text-[10px] font-bold text-brand-sky uppercase bg-brand-skyLight px-2.5 py-1 rounded-full">${badge}</span>
                            <span class="text-[11px] text-slate-400 font-medium">⏱️ ${g.read_time || '5 min read'}</span>
                        </div>
                        <h4 class="text-base font-bold text-brand-dark group-hover:text-brand-sky transition line-clamp-2 mb-2">
                            <a href="${link}">${g.title}</a>
                        </h4>
                        <p class="text-xs text-slate-500 leading-relaxed line-clamp-3 mb-4">
                            ${g.meta_description}
                        </p>
                    </div>
                    <div class="pt-4 border-t border-slate-100 flex items-center justify-between text-xs">
                        <a href="${link}" class="font-bold text-brand-sky hover:text-brand-skyHover flex items-center gap-1">
                            <span>Read Full Guide</span>
                            <span>&rarr;</span>
                        </a>
                        <a href="${waLink}" target="_blank" rel="noopener noreferrer" class="font-semibold text-emerald-600 hover:text-emerald-700">
                            Ask CA 💬
                        </a>
                    </div>
                </div>
            `;
        }).join('');
    }

    /**
     * Render FAQs into an accordion container
     */
    function renderFaqs(container, faqs) {
        if (!container || !faqs || faqs.length === 0) return;

        container.innerHTML = faqs.map((faq, idx) => `
            <div class="border border-slate-200 rounded-xl overflow-hidden bg-white mb-3">
                <button onclick="CraftegonKnowledgeHub.toggleFaq(${idx})" class="w-full text-left px-5 py-4 font-bold text-xs sm:text-sm text-brand-dark flex items-center justify-between hover:bg-slate-50 transition">
                    <span>${faq.question}</span>
                    <span id="ckh-faq-icon-${idx}" class="text-slate-400 font-bold ml-2 transition-transform transform">▼</span>
                </button>
                <div id="ckh-faq-answer-${idx}" class="hidden px-5 pb-4 text-xs sm:text-sm text-slate-600 leading-relaxed border-t border-slate-100 pt-3">
                    ${faq.answer}
                </div>
            </div>
        `).join('');
    }

    function toggleFaq(index) {
        const answer = document.getElementById(`ckh-faq-answer-${index}`);
        const icon = document.getElementById(`ckh-faq-icon-${index}`);
        if (answer) {
            const isHidden = answer.classList.contains('hidden');
            answer.classList.toggle('hidden');
            if (icon) {
                icon.style.transform = isHidden ? 'rotate(180deg)' : 'rotate(0deg)';
            }
        }
    }

    /**
     * Auto-detect and populate containers on the page
     */
    async function autoInit() {
        const guides = await fetchGuides();
        const currentCat = detectCurrentCategory();

        // 1. Check known specific guide containers
        const containerMappings = [
            { id: 'incorporation-articles', cat: 'business-setup', regex: /company|incorporation|pvt|llp|registration/i },
            { id: 'gst-articles', cat: 'gst-advisory', regex: /gst|gstr|tax|return/i },
            { id: 'trademark-articles', cat: 'brand-protection', regex: /trademark|tm|brand|ip/i },
            { id: 'license-articles', cat: 'business-setup', regex: /fssai|license|msme|udyam/i },
            { id: 'contact-knowledge-articles', cat: 'all', regex: null },
            { id: 'knowledge-hub-container', cat: currentCat, regex: null }
        ];

        containerMappings.forEach(({ id, cat, regex }) => {
            const el = document.getElementById(id);
            if (!el) return;

            let filtered = guides;
            if (regex) {
                filtered = guides.filter(g => regex.test(g.title) || regex.test(g.meta_description) || g.category === cat);
            } else if (cat && cat !== 'all') {
                filtered = guides.filter(g => g.category === cat);
            }

            renderCards(el, filtered.slice(0, 6));
        });

        // 2. Check FAQ accordion containers
        const faqContainer = document.getElementById('faq-accordion') || document.getElementById('knowledge-faqs');
        if (faqContainer) {
            const allFaqs = [];
            guides.forEach(g => {
                if (currentCat === 'all' || g.category === currentCat) {
                    if (g.faqs) allFaqs.push(...g.faqs);
                }
            });
            if (allFaqs.length > 0) {
                renderFaqs(faqContainer, allFaqs.slice(0, 6));
            }
        }
    }

    // Public API
    return {
        load: async function (opts = {}) {
            const guides = await fetchGuides();
            const container = document.getElementById(opts.containerId);
            if (!container) return;

            let matched = guides;
            if (opts.keywordRegex) {
                matched = guides.filter(g => opts.keywordRegex.test(g.title) || opts.keywordRegex.test(g.meta_description));
            } else if (opts.category) {
                matched = guides.filter(g => g.category === opts.category);
            }

            renderCards(container, matched.slice(0, opts.maxCount || 6));
        },
        toggleFaq,
        fetchGuides,
        autoInit
    };
})();

// Attach to window and auto-run on DOMContentLoaded
if (typeof window !== 'undefined') {
    window.CraftegonKnowledgeHub = CraftegonKnowledgeHub;
    document.addEventListener('DOMContentLoaded', () => {
        CraftegonKnowledgeHub.autoInit();
    });
}
