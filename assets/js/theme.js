"use strict";

/** Applique le thème mémorisé avant l’affichage et initialise son interrupteur. */
(() => {
    const StorageKey = "site-theme";
    const root = document.documentElement;
    let selected = "light";
    try {
        if (localStorage.getItem(StorageKey) === "dark") {
            selected = "dark";
        }
    } catch {
        // Le changement reste utilisable lorsque le stockage est indisponible.
    }
    root.dataset.theme = selected;
    root.classList.add("theme-ready");

    document.addEventListener("DOMContentLoaded", () => {
        const button = document.querySelector(".theme-toggle");
        if (!button) {
            return;
        }
        /** Synchronise le thème, l’état accessible et l’indication de l’action. */
        function applyTheme(theme) {
            root.dataset.theme = theme;
            const dark = theme === "dark";
            button.setAttribute("aria-checked", String(dark));
            button.title = dark ? "Passer au mode clair" : "Passer au mode sombre";
        }
        applyTheme(root.dataset.theme);
        button.addEventListener("click", () => {
            const theme = root.dataset.theme === "dark" ? "light" : "dark";
            applyTheme(theme);
            try {
                localStorage.setItem(StorageKey, theme);
            } catch {
                // Sans stockage, le thème choisi reste actif sur la page courante.
            }
        });
        window.addEventListener("storage", (event) => {
            if (event.key === StorageKey) {
                applyTheme(event.newValue === "dark" ? "dark" : "light");
            }
        });
    });
})();
