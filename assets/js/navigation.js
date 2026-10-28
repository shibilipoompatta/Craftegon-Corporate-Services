/**
 * CraftEgon Corporate Services (CCS) - Navigation & Service Catalog Interactive Engine
 * Handles Category Switching, Service Card Filtering, Live Search, Modal Sync, and Lucide Icon Init
 */

const CATEGORY_METADATA = {
    all: {
        title: "All 60 Specialized Services",
        tagline: "Comprehensive LegalTech, Tax & Regulatory Hub for Indian & Global Enterprises",
        badge: "60 Available Services",
        icon: "layout-grid"
    },
    formation: {
        title: "Business Setup & Formation",
        tagline: "Entity Structuring, Incorporation & Capital Setup",
        badge: "10 Formation Services",
        icon: "building-2"
    },
    gst: {
        title: "GST Advisory & Filings",
        tagline: "End-to-End Indirect Tax Management & Notice Defense",
        badge: "10 GST Solutions",
        icon: "badge-percent"
    },
    mca: {
        title: "Corporate Secretarial & Regulatory Governance",
        tagline: "Statutory MCA Compliance, Risk Management & Retainers",
        badge: "10 Secretarial Services",
        icon: "landmark"
    },
    tax: {
        title: "Direct Tax & Income Tax Services",
        tagline: "Corporate Tax Planning, TDS & Regulatory Advisory",
        badge: "10 Tax Solutions",
        icon: "receipt"
    },
    ipr: {
        title: "Brand & IP Protection",
        tagline: "Trademark, Patent, Copyright & Brand Asset Protection",
        badge: "10 IP Protections",
        icon: "sparkles"
    },
    digital: {
        title: "Workforce Management & Digital Infrastructure",
        tagline: "HR Labour Compliance, Legal Contracts & AI/Digital Systems",
        badge: "10 Infrastructure Services",
        icon: "cpu"
    }
};

let activeCategory = 'all';
let searchQuery = '';

document.addEventListener('DOMContentLoaded', () => {
    initServiceCatalog();
    initInquiryModal();
    initSmoothScrolling();
    
    // Initial Lucide icon generation
    if (window.lucide) {
        window.lucide.createIcons();
    }
});

/**
 * Initializes the tab filters, quick search, and category header updates
 */
function initServiceCatalog() {
    const filterButtons = document.querySelectorAll('[data-category-filter]');
    const searchInput = document.getElementById('catalog-search-input');
    const clearSearchBtn = document.getElementById('clear-search-btn');

    // Category button click handlers
    filterButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const category = btn.getAttribute('data-category-filter');
            setActiveCategory(category);
        });
    });

    // Live search input handler
    if (searchInput) {
        searchInput.addEventListener('input', (e) => {
            searchQuery = e.target.value.toLowerCase().trim();
            if (clearSearchBtn) {
                clearSearchBtn.classList.toggle('hidden', searchQuery.length === 0);
            }
            filterServices();
        });
    }

    // Clear search button handler
    if (clearSearchBtn && searchInput) {
        clearSearchBtn.addEventListener('click', () => {
            searchInput.value = '';
            searchQuery = '';
            clearSearchBtn.classList.add('hidden');
            filterServices();
        });
    }
}

/**
 * Switch active category tab and trigger filter update
 */
function setActiveCategory(category) {
    if (!CATEGORY_METADATA[category]) return;
    activeCategory = category;

    // Update Tab Button Visual Styles
    const filterButtons = document.querySelectorAll('[data-category-filter]');
    filterButtons.forEach(btn => {
        const cat = btn.getAttribute('data-category-filter');
        const isActive = cat === category;

        if (isActive) {
            btn.className = "category-tab-btn active px-4 py-2.5 rounded-xl text-xs md:text-sm font-bold transition-all duration-300 flex items-center gap-2 whitespace-nowrap bg-gradient-to-r from-gold-500/20 via-gold-400/15 to-transparent text-gold-400 border border-gold-500 shadow-[0_0_15px_rgba(197,160,89,0.2)]";
        } else {
            btn.className = "category-tab-btn px-4 py-2.5 rounded-xl text-xs md:text-sm font-semibold transition-all duration-300 flex items-center gap-2 whitespace-nowrap bg-[#111827]/80 text-slate-400 border border-slate-800/80 hover:text-white hover:border-slate-700 hover:bg-[#162033]";
        }
    });

    // Update Header Metadata Showcase
    const meta = CATEGORY_METADATA[category];
    const hubTitleEl = document.getElementById('active-category-title');
    const hubTaglineEl = document.getElementById('active-category-tagline');
    const hubBadgeEl = document.getElementById('active-category-badge');

    if (hubTitleEl) hubTitleEl.innerText = meta.title;
    if (hubTaglineEl) hubTaglineEl.innerText = meta.tagline;
    if (hubBadgeEl) hubBadgeEl.innerText = meta.badge;

    filterServices();
}

/**
 * Filters the 60 service cards based on category and search query
 */
function filterServices() {
    const cards = document.querySelectorAll('.service-card-item');
    const noResultsEl = document.getElementById('catalog-no-results');
    const resultsCountEl = document.getElementById('catalog-results-count');
    let visibleCount = 0;

    cards.forEach(card => {
        const cardCategory = card.getAttribute('data-category');
        const cardTitle = (card.getAttribute('data-title') || '').toLowerCase();
        const cardKeywords = (card.getAttribute('data-keywords') || '').toLowerCase();
        const cardDesc = (card.innerText || '').toLowerCase();

        const matchesCategory = (activeCategory === 'all' || cardCategory === activeCategory);
        const matchesSearch = !searchQuery || 
            cardTitle.includes(searchQuery) || 
            cardKeywords.includes(searchQuery) || 
            cardDesc.includes(searchQuery);

        if (matchesCategory && matchesSearch) {
            card.classList.remove('hidden');
            card.classList.add('flex');
            visibleCount++;
        } else {
            card.classList.add('hidden');
            card.classList.remove('flex');
        }
    });

    // Show/hide empty state
    if (noResultsEl) {
        noResultsEl.classList.toggle('hidden', visibleCount > 0);
    }

    if (resultsCountEl) {
        resultsCountEl.innerText = `Showing ${visibleCount} of 60 services`;
    }

    // Refresh icons if needed
    if (window.lucide) {
        window.lucide.createIcons();
    }
}

/**
 * Inquiry & Consultation Booking Modal Controller
 */
function initInquiryModal() {
    const modal = document.getElementById('inquiry-modal');
    if (!modal) return;

    // Attach click listeners to all Inquiry buttons
    document.addEventListener('click', (e) => {
        const trigger = e.target.closest('[data-action="inquire"]');
        if (trigger) {
            e.preventDefault();
            const serviceName = trigger.getAttribute('data-service') || 'General Corporate Consultation';
            const fee = trigger.getAttribute('data-fee') || 'Bespoke';
            const category = trigger.getAttribute('data-category') || 'General';
            openInquiryModal(serviceName, fee, category);
        }
    });

    // Modal Close Button
    const closeBtn = document.getElementById('close-inquiry-modal-btn');
    if (closeBtn) {
        closeBtn.addEventListener('click', closeInquiryModal);
    }

    // Click outside backdrop
    modal.addEventListener('click', (e) => {
        if (e.target === modal) {
            closeInquiryModal();
        }
    });

    // Escape key listener
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && !modal.classList.contains('hidden')) {
            closeInquiryModal();
        }
    });

    // Modal Form Submission Handler
    const modalForm = document.getElementById('inquiry-modal-form');
    if (modalForm) {
        modalForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const serviceName = document.getElementById('modal-service-input')?.value || 'Service Consultation';
            const submitBtn = modalForm.querySelector('button[type="submit"]');
            const originalText = submitBtn ? submitBtn.innerHTML : 'Confirm Request';

            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = `<span>Connecting with Legal Desk...</span>`;
            }

            setTimeout(() => {
                alert(`Thank you! Your inquiry for "${serviceName}" has been routed to our corporate desk. A dedicated CA/CS will connect with you within 10 minutes.`);
                modalForm.reset();
                if (submitBtn) {
                    submitBtn.disabled = false;
                    submitBtn.innerHTML = originalText;
                }
                closeInquiryModal();
            }, 700);
        });
    }
}

/**
 * Opens the consultation modal and pre-fills service data
 */
function openInquiryModal(serviceName, fee = 'Bespoke', category = '') {
    const modal = document.getElementById('inquiry-modal');
    if (!modal) return;

    const titleEl = document.getElementById('modal-selected-service-title');
    const feeEl = document.getElementById('modal-selected-service-fee');
    const inputEl = document.getElementById('modal-service-input');
    const categoryEl = document.getElementById('modal-selected-category');

    if (titleEl) titleEl.innerText = serviceName;
    if (feeEl) feeEl.innerText = fee;
    if (inputEl) inputEl.value = serviceName;
    if (categoryEl) categoryEl.innerText = category;

    modal.classList.remove('hidden');
    modal.classList.add('flex');
    document.body.classList.add('overflow-hidden');

    // Also update WhatsApp link with specific service query
    const waBtn = document.getElementById('modal-whatsapp-link');
    if (waBtn) {
        const text = encodeURIComponent(`Hello Craftegon Team, I am inquiring about *${serviceName}* (${fee}). Please connect me with a consultant.`);
        waBtn.href = `https://wa.me/918606918247?text=${text}`;
    }

    if (window.lucide) {
        window.lucide.createIcons();
    }
}

/**
 * Closes the consultation modal
 */
function closeInquiryModal() {
    const modal = document.getElementById('inquiry-modal');
    if (!modal) return;

    modal.classList.add('hidden');
    modal.classList.remove('flex');
    document.body.classList.remove('overflow-hidden');
}

/**
 * Smooth scrolling helper
 */
function initSmoothScrolling() {
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#' || targetId.startsWith('#!')) return;
            const target = document.querySelector(targetId);
            if (target) {
                e.preventDefault();
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// Expose functions globally for inline onclick handlers if needed
window.CCSNavigation = {
    setActiveCategory,
    openInquiryModal,
    closeInquiryModal,
    filterServices
};
