"use strict";

/** Initialise la navigation et la recherche après le contenu de la page. */
function initializeSite() {
	const container = document.querySelector(".flex-container");
	const menuButton = document.querySelector(".menu-icon");
	const searchButton = document.querySelector(".search-icon");
	const searchBox = document.querySelector(".search-box");
	const searchInput = document.getElementById("search-input");

	/** Ferme les panneaux et synchronise les indications d’accessibilité. */
	function closePanels() {
		container?.classList.remove("active");
		searchBox?.classList.remove("search-active");
		menuButton?.setAttribute("aria-expanded", "false");
		searchButton?.setAttribute("aria-expanded", "false");
	}

	menuButton?.addEventListener("click", () => {
		const opened = container.classList.toggle("active");
		menuButton.setAttribute("aria-expanded", String(opened));
	});
	document.querySelector(".menu-icon-close")?.addEventListener("click", closePanels);
	searchButton?.addEventListener("click", () => {
		const opened = searchBox.classList.toggle("search-active");
		searchButton.setAttribute("aria-expanded", String(opened));
		if (opened) {
			searchInput.focus();
		}
	});
	document.querySelector(".search-icon-close")?.addEventListener("click", () => {
		closePanels();
		searchButton.focus();
	});
	document.addEventListener("keydown", (event) => {
		if (event.key === "Escape") {
			const searching = searchBox?.classList.contains("search-active");
			closePanels();
			(searching ? searchButton : menuButton)?.focus();
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

	// Le portfolio partage la même configuration pour ses cinq galeries.
	if (document.querySelector(".carousel")) {
		jQuery(".carousel").each(function () {
			jQuery(this).carousel({
				effect: "fade",
				markers: {
					show: true,
					type: "cycle",
					position: this.id === "CarouselVideo" ? "top-center" : "bottom-center"
				}
			});
		});
	}
	if (document.querySelector("[data-lightbox]")) {
		lightbox.option({ wrapAround: true });
	}
}

initializeSite();
