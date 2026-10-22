/**
 * Shared Fetch Engine for Craftegon Knowledge Hub
 */
async function loadKnowledgeArticles({ containerId, keywordRegex, fallbackArticles, maxCount = 6 }) {
    const container = document.getElementById(containerId);
    if (!container) return;

    try {
        const response = await fetch('data/indiafilings-knowledge-hub.json');
        if (!response.ok) throw new Error(`HTTP error! status: ${response.status}`);
        
        const data = await response.json();
        const blogs = data.blog_pages || data.blogs || [];

        let matchedGuides = blogs;
        if (keywordRegex) {
            matchedGuides = blogs.filter(b => {
                const title = typeof b === 'string' ? b : (b.title || b.name || '');
                return keywordRegex.test(title);
            });
        }

        const selectedGuides = matchedGuides.length > 0 
            ? matchedGuides.slice(0, maxCount) 
            : (fallbackArticles || blogs.slice(0, maxCount));

        renderKnowledgeCards(container, selectedGuides, fallbackArticles);
    } catch (err) {
        console.warn(`Knowledge Hub Engine: Using fallback data for ${containerId}`, err);
        renderKnowledgeCards(container, fallbackArticles || [], fallbackArticles);
    }
}

function renderKnowledgeCards(container, guides, fallbackGuides) {
    const finalGuides = (guides && guides.length > 0) ? guides : fallbackGuides;

    if (!finalGuides || finalGuides.length === 0) {
        container.innerHTML = `<div class="col-span-full text-center py-8 text-slate-400 text-sm">No articles available at the moment.</div>`;
        return;
    }

    container.innerHTML = finalGuides.map(guide => {
        const title = typeof guide === 'string' ? guide : (guide.title || guide.name || 'Legal & Regulatory Manual');
        const summary = guide.summary || guide.description || 'Learn key compliance requirements, statutory portal procedures, and legal guidelines.';
        const url = guide.url || '#';

        return `
            <div class="bg-white p-6 rounded-2xl border border-slate-200 shadow-sm hover:shadow-md transition flex flex-col justify-between">
                <div>
                    <span class="text-[10px] font-bold text-sky-600 uppercase bg-sky-100 px-2.5 py-1 rounded-full">Legal Manual</span>
                    <h4 class="text-base font-bold text-slate-900 mt-3 mb-2 line-clamp-2">${title}</h4>
                    <p class="text-xs text-slate-500 leading-relaxed line-clamp-3">${summary}</p>
                </div>
                <a href="${url}" ${url !== '#' ? 'target="_blank"' : ''} class="mt-5 text-xs font-bold text-sky-600 hover:text-sky-700 flex items-center gap-1">
                    <span>Read Full Guide</span>
                    <span>&rarr;</span>
                </a>
            </div>
        `;
    }).join('');
}

// Global hook so individual pages can initialize effortlessly
window.CraftegonKnowledgeHub = { load: loadKnowledgeArticles };