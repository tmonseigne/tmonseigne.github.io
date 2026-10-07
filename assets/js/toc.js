"use strict";

/** Place le sommaire généré par Kramdown dans la colonne adaptée à l’écran. */
function initializePostToc() {
	const layout = document.querySelector(".post-layout");
	const content = layout?.querySelector(".post-content");
	const list = content?.querySelector("ul.toc-post");
	if (!list) {
		return;
	}

	const navigation = document.createElement("nav");
	navigation.className = "post-toc";
	navigation.setAttribute("aria-label", "Sommaire");
	const title = document.createElement("p");
	title.className = "post-toc-title";
	title.textContent = "Sommaire";
	list.before(navigation);
	navigation.append(title, list);

	const wideScreen = window.matchMedia("(min-width: 1200px)");
	/** Déplace le même sommaire, sans dupliquer ses liens ni ses identifiants. */
	function updateTocPlacement() {
		document.documentElement.classList.toggle("post-with-toc", wideScreen.matches);
		if (wideScreen.matches) {
			layout.prepend(navigation);
		} else {
			content.prepend(navigation);
		}
	}

	layout.classList.add("has-toc");
	wideScreen.addEventListener("change", updateTocPlacement);
	updateTocPlacement();
}

initializePostToc();
