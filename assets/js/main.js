/**
 * Main Application Logic & Interactivity
 */
document.addEventListener('DOMContentLoaded', () => {
    initLeadForms();
    initMobileNav();
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
