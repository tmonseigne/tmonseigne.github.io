"use strict";

/** Initialise une galerie autonome : navigation, clavier et défilement automatique des médias. */
function initializeCarousel(carousel) {
	const slides = [...carousel.querySelectorAll(".slide")];
	if (!slides.length) {
		return;
	}
	const hasVideos = Boolean(carousel.querySelector("video"));
	const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
	const SlideInterval = 2000;
	const FadeDuration = 1000;
	let transitionSequence = 0;
	let index = 0;
	let timer = null;
	let visible = false;
	let paused = false;
	const title = carousel.closest("section")?.querySelector("h1")?.textContent || "Galerie";
	carousel.setAttribute("role", "region");
	carousel.setAttribute("aria-roledescription", "carrousel");
	carousel.setAttribute("aria-label", title);
	carousel.tabIndex = 0;

	const markers = document.createElement("div");
	markers.className = "markers";
	const list = document.createElement("ul");
	markers.append(list);
	carousel.append(markers);
	const buttons = slides.map((slide, number) => {
		const item = document.createElement("li");
		const button = document.createElement("button");
		button.type = "button";
		button.setAttribute("aria-label", `Afficher l’aperçu ${number + 1} sur ${slides.length}`);
		button.addEventListener("click", () => showSlide(number));
		item.append(button);
		list.append(item);
		slide.setAttribute("role", "group");
		slide.setAttribute("aria-label", `Aperçu ${number + 1} sur ${slides.length}`);
		return button;
	});

	/** Arrête le minuteur avant chaque modification de son état. */
	function stopTimer() {
		window.clearInterval(timer);
		timer = null;
	}

	/** Ne défile pas pendant une interaction, hors écran ou sous une image agrandie. */
	function refreshTimer() {
		stopTimer();
		const playing = [...slides[index].querySelectorAll("video")].some(video => !video.paused && !video.ended);
		if (playing || paused || reducedMotion.matches || !visible || document.hidden ||
			carousel.matches(":hover") || carousel.contains(document.activeElement) ||
			document.body.classList.contains("lb-disable-scrolling")) {
			return;
		}
		timer = window.setInterval(() => showSlide(index + 1), SlideInterval);
	}

	/** Superpose les deux images pendant le fondu, sans passage par un fond blanc. */
	function showSlide(nextIndex) {
		const previous = slides[index];
		index = (nextIndex + slides.length) % slides.length;
		const current = slides[index];
		const sequence = ++transitionSequence;
		const fading = previous !== current && !reducedMotion.matches;
		if (previous !== current) {
			previous.querySelectorAll("video").forEach(video => video.pause());
		}
		slides.forEach((slide, number) => {
			// Une nouvelle commande interrompt proprement la transition précédente.
			slide.getAnimations().forEach(animation => animation.cancel());
			slide.hidden = slide !== current && !(fading && slide === previous);
			slide.inert = slide !== current;
			slide.setAttribute("aria-hidden", String(slide !== current));
			slide.classList.toggle("is-current", slide === current);
			buttons[number].setAttribute("aria-current", String(number === index));
		});
		if (fading) {
			// L’image précédente reste opaque sous la nouvelle jusqu’à la fin du fondu.
			const animation = current.animate([{opacity: 0}, {opacity: 1}], {
				duration: FadeDuration,
				easing: "ease-in-out"
			});
			animation.finished.then(() => {
				if (sequence === transitionSequence) {
					previous.hidden = true;
				}
			}).catch(() => {
				// Une navigation rapide annule normalement l’animation en cours.
			});
		}
		refreshTimer();
	}

	carousel.querySelector(".controls.left")?.addEventListener("click", () => showSlide(index - 1));
	carousel.querySelector(".controls.right")?.addEventListener("click", () => showSlide(index + 1));
	carousel.addEventListener("keydown", event => {
		// Les commandes natives de la vidéo conservent leurs raccourcis.
		if (event.target.closest("video") || event.altKey || event.ctrlKey || event.metaKey) {
			return;
		}
		const positions = {ArrowLeft: index - 1, ArrowRight: index + 1, Home: 0, End: slides.length - 1};
		if (Object.hasOwn(positions, event.key)) {
			event.preventDefault();
			showSlide(positions[event.key]);
		}
	});
	if (slides.length > 1) {
		const pauseButton = document.createElement("button");
		pauseButton.type = "button";
		pauseButton.className = "carousel-pause";
		/** Présente explicitement l’action disponible au lecteur. */
		function updatePauseButton() {
			pauseButton.textContent = paused ? "▶" : "Ⅱ";
			pauseButton.setAttribute("aria-label", paused ? "Reprendre le diaporama" : "Mettre le diaporama en pause");
			pauseButton.setAttribute("aria-pressed", String(paused));
		}
		pauseButton.addEventListener("click", () => {
			paused = !paused;
			updatePauseButton();
			refreshTimer();
		});
		updatePauseButton();
		carousel.append(pauseButton);
	}
	// La lecture suspend le diaporama ; une pause ou une fin de vidéo le relance.
	carousel.querySelectorAll("video").forEach(video => {
		video.addEventListener("play", stopTimer);
		video.addEventListener("pause", refreshTimer);
		video.addEventListener("ended", refreshTimer);
	});
	carousel.classList.toggle("carousel-video", hasVideos);
	carousel.addEventListener("mouseenter", stopTimer);
	carousel.addEventListener("mouseleave", refreshTimer);
	carousel.addEventListener("focusin", stopTimer);
	carousel.addEventListener("focusout", () => window.setTimeout(refreshTimer, 0));
	document.addEventListener("visibilitychange", refreshTimer);
	reducedMotion.addEventListener("change", refreshTimer);
	// Lightbox ajoute cette classe à l’ouverture et la retire à la fermeture.
	new MutationObserver(refreshTimer).observe(document.body, {attributes: true, attributeFilter: ["class"]});
	new IntersectionObserver(entries => {
		visible = entries[0].isIntersecting;
		if (!visible) {
			slides[index].querySelectorAll("video").forEach(video => video.pause());
		}
		refreshTimer();
	}, {threshold: 0.1}).observe(carousel);
	showSlide(0);
}

document.querySelectorAll(".carousel").forEach(initializeCarousel);
