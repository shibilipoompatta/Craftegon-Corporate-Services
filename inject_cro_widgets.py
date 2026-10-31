"""
inject_cro_widgets.py
Injects the unified Mobile Sticky Bottom Bar and Desktop Floating WhatsApp Widget
into all HTML pages and updates Python build templates.
"""

import os
import glob
import re

WIDGETS_HTML = """
    <!-- Unified Mobile Sticky Bottom Action Bar (<768px) -->
    <div id="ccs-mobile-sticky-bar" class="md:hidden fixed bottom-0 left-0 right-0 z-40 bg-white/95 backdrop-blur-md border-t border-slate-200 px-4 py-2.5 flex items-center gap-3 shadow-2xl">
        <a href="tel:+918606918247" class="flex-1 bg-slate-100 hover:bg-slate-200 text-slate-800 font-extrabold text-xs py-3 px-3 rounded-xl border border-slate-200 flex items-center justify-center gap-2 transition min-touch">
            <svg class="w-4 h-4 text-brand-sky" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
            <span>Talk to CA/CS</span>
        </a>
        <a href="https://wa.me/918606918247?text=Hi%20Craftegon,%20I%20need%20assistance%20with%20corporate%20compliance" target="_blank" rel="noopener noreferrer" class="flex-1 bg-[#25D366] hover:bg-[#20bd5a] text-white font-extrabold text-xs py-3 px-3 rounded-xl shadow-md flex items-center justify-center gap-2 transition min-touch">
            <svg class="w-4 h-4 fill-current" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
            <span>Instant WhatsApp</span>
        </a>
    </div>

    <!-- Desktop Floating WhatsApp Widget (>=768px) -->
    <aside id="ccs-desktop-floating-cta" aria-label="WhatsApp Consultation Support" class="hidden md:block fixed bottom-6 right-6 z-40">
        <a href="https://wa.me/918606918247?text=Hi%20Craftegon,%20I%20need%20assistance%20with%20corporate%20compliance" target="_blank" rel="noopener noreferrer" aria-label="Chat with CA/CS on WhatsApp" class="flex items-center gap-3 bg-[#25D366] hover:bg-[#20bd5a] text-white px-4 py-3 rounded-full shadow-2xl hover:shadow-emerald-500/30 transition-all duration-300 hover:scale-105 group">
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
"""

def update_html_files():
    html_files = glob.glob('*.html') + glob.glob('**/*.html', recursive=True)
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = False

        # 1. Add pb-16 md:pb-0 to body if not present
        if '<body' in content and 'pb-16' not in content:
            content = re.sub(r'(<body[^>]*class="[^"]*)(")', r'\1 pb-16 md:pb-0\2', content)
            updated = True

        # 2. Add config.js before forms.js or main.js if not present
        if '/assets/js/config.js' not in content:
            if '<script src="/assets/js/forms.js">' in content:
                content = content.replace('<script src="/assets/js/forms.js">', '<script src="/assets/js/config.js"></script>\n    <script src="/assets/js/forms.js">')
                updated = True
            elif '<script src="/assets/js/main.js">' in content:
                content = content.replace('<script src="/assets/js/main.js">', '<script src="/assets/js/config.js"></script>\n    <script src="/assets/js/main.js">')
                updated = True

        # 3. Add WIDGETS_HTML right after </footer> if not present
        if 'ccs-mobile-sticky-bar' not in content and '</footer>' in content:
            content = content.replace('</footer>', '</footer>\n' + WIDGETS_HTML)
            updated = True

        if updated:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            count += 1
            print(f"Injected CRO widgets into: {filepath}")

    print(f"Updated {count} HTML files.")

def update_python_builders():
    builders = ['build_knowledge_pages.py', 'build_legal_pages.py', 'build_category_hubs.py', 'build_product_pages.py']
    for b in builders:
        if not os.path.exists(b):
            continue
        with open(b, 'r', encoding='utf-8') as f:
            content = f.read()

        updated = False
        # Inject widgets into FOOTER_HTML or GLOBAL_FOOTER if not present
        if 'ccs-mobile-sticky-bar' not in content:
            if '</footer>"""' in content:
                content = content.replace('</footer>"""', '</footer>\n' + WIDGETS_HTML + '"""')
                updated = True
            elif '</footer>\n"""' in content:
                content = content.replace('</footer>\n"""', '</footer>\n' + WIDGETS_HTML + '\n"""')
                updated = True

        # Inject config.js before forms.js
        if '/assets/js/config.js' not in content and '<script src="/assets/js/forms.js">' in content:
            content = content.replace('<script src="/assets/js/forms.js">', '<script src="/assets/js/config.js"></script>\n<script src="/assets/js/forms.js">')
            updated = True

        if updated:
            with open(b, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated Python builder: {b}")

if __name__ == '__main__':
    update_html_files()
    update_python_builders()

