"use strict";

/** Configuration MathJax 4 : TeX courant et anciennes balises utilisées dans les articles. */
window.MathJax = {
	tex: {
		inlineMath: [["\\(", "\\)"]],
		displayMath: [["\\[", "\\]"], ["$$", "$$"]],
		tags: "none",
		useLabelIds: true
	},
	options: {
		renderActions: {
			// Complète la recherche standard, sans modifier les textes ni le Markdown des articles.
			findScript: [10, documentMath => {
				for (const node of document.querySelectorAll('script[type^="math/tex"]')) {
					const display = /;\s*mode=display/.test(node.type);
					const math = new documentMath.options.MathItem(node.textContent, documentMath.inputJax[0], display);
					const text = document.createTextNode("");
					node.replaceWith(text);
					math.start = {node: text, delim: "", n: 0};
					math.end = {node: text, delim: "", n: 0};
					documentMath.math.push(math);
				}
			}, ""]
		}
	}
};
