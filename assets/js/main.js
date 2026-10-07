"use strict";

/** Initialise la navigation et la recherche après le contenu de la page. */
function initializeSite() {
	const searchButton = document.querySelector(".search-icon");
	const searchBox = document.querySelector(".search-box");
	const searchInput = document.getElementById("search-input");

	/** Ferme la recherche et synchronise son indication d’accessibilité. */
	function closeSearch() {
		searchBox?.classList.remove("search-active");
		searchButton?.setAttribute("aria-expanded", "false");
	}

	searchButton?.addEventListener("click", () => {
		const opened = searchBox.classList.toggle("search-active");
		searchButton.setAttribute("aria-expanded", String(opened));
		if (opened) {
			searchInput.focus();
		}
	});
	document.querySelector(".search-icon-close")?.addEventListener("click", () => {
		closeSearch();
		searchButton.focus();
	});
	document.addEventListener("keydown", (event) => {
		if (event.key === "Escape" && searchBox?.classList.contains("search-active") &&
			!document.body.classList.contains("lb-disable-scrolling")) {
			closeSearch();
			searchButton?.focus();
		}
	});
	document.querySelector(".search-form")?.addEventListener("submit", (event) => event.preventDefault());

	if (searchInput) {
		/** Échappe les métadonnées avant leur insertion dans les résultats HTML. */
		function escapeHtml(value) {
			const text = document.createElement("span");
			text.textContent = value;
			return text.innerHTML.replaceAll('"', "&quot;");
		}
		SimpleJekyllSearch({
			searchInput,
			resultsContainer: document.getElementById("results-container"),
			json: searchInput.dataset.searchUrl,
			searchResultTemplate: '<li><a href="{url}">{title}</a></li>',
			templateMiddleware: (property, value) => escapeHtml(value),
			noResultsText: "Aucun résultat",
			fuzzy: false
		});
	}

	if (document.querySelector("[data-lightbox]")) {
		lightbox.option({
			wrapAround: true,
			disableScrolling: true,
			albumLabel: "Image %1 sur %2",
			fadeDuration: 200,
			imageFadeDuration: 200,
			resizeDuration: 200
		});
	}
}

initializeSite();
