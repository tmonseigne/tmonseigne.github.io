/** Alphabet de référence des substitutions monoalphabétiques. */
export const Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

/** Alphabets historiques utilisés par l’assistant ; chacun est une permutation de A à Z. */
export const PresetAlphabets = Object.freeze({
	Atbash: "ZYXWVUTSRQPONMLKJIHGFEDCBA",
	Albam: "NOPQRSTUVWXYZABCDEFGHIJKLM",
	Atbah: "IHGFNDCBARQPOEMLKJZYXWVUTS",
	Kendorimien: "ECDFIGHJOKLMNPUQRSTVYWXZAB"
});

/** Retire les accents, en conservant la casse, les espaces et la ponctuation. */
export function normalizeText(text) {
	return text.normalize("NFD").replace(/[\u0300-\u036f]/g, "");
}

/** Construit une permutation par décalage entier, positif ou négatif. */
export function getCaesarAlphabet(shift) {
	if (!Number.isSafeInteger(shift)) {
		throw new Error("Indiquez un décalage entier valide.");
	}
	const offset = ((shift % Alphabet.length) + Alphabet.length) % Alphabet.length;
	return Alphabet.slice(offset) + Alphabet.slice(0, offset);
}

/** Déduplique les lettres de la clé puis complète la grille avec les lettres restantes. */
export function getGridAlphabet(key, vertical = false) {
	const letters = normalizeText(key).toUpperCase().replace(/[^A-Z]/g, "");
	const prefix = [...new Set(letters)].join("");
	const grid = [...new Set(prefix + Alphabet)].join("");
	if (!vertical) {
		return grid;
	}
	if (prefix.length === 0) {
		throw new Error("Indiquez au moins une lettre pour la grille verticale.");
	}

	// La largeur est le nombre de lettres distinctes de la clé ; lecture par colonnes.
	let result = "";
	for (let column = 0; column < prefix.length; ++column) {
		for (let index = column; index < grid.length; index += prefix.length) {
			result += grid[index];
		}
	}
	return result;
}

/** Substitue les lettres en préservant leur casse ; inverse la correspondance au déchiffrement. */
export function substitute(text, cipherAlphabet, decrypt = false) {
	if (cipherAlphabet.length !== Alphabet.length ||
		new Set(cipherAlphabet).size !== Alphabet.length ||
		/[^A-Z]/.test(cipherAlphabet)) {
		throw new Error("La grille doit contenir exactement les 26 lettres, sans doublon.");
	}
	const source = decrypt ? cipherAlphabet : Alphabet;
	const target = decrypt ? Alphabet : cipherAlphabet;
	let result = "";
	for (const character of normalizeText(text)) {
		const index = source.indexOf(character.toUpperCase());
		if (index === -1) {
			result += character;
		} else {
			const replacement = target[index];
			result += character === character.toLowerCase() ? replacement.toLowerCase() : replacement;
		}
	}
	return result;
}

/** Applique les options de présentation ; le générateur aléatoire est injectable pour les tests. */
export function formatText(text, {letterCase = "unchanged", spacing = "unchanged"} = {}, random = Math.random) {
	let result = text;
	if (letterCase === "upper") {
		result = result.toUpperCase();
	} else if (letterCase === "lower") {
		result = result.toLowerCase();
	} else if (letterCase === "random") {
		result = [...result].map(character => random() >= 0.5 ? character.toUpperCase() : character.toLowerCase()).join("");
	}
	if (spacing === "unchanged") {
		return result;
	}

	// Comme dans l’outil d’origine, seuls les espaces ordinaires sont regroupés.
	const compact = result.replaceAll(" ", "");
	if (spacing === "random") {
		return [...compact].map(character => character + (random() >= 0.75 ? " " : "")).join("");
	}
	const size = spacing === "blocks4" ? 4 : 5;
	const blocks = [];
	for (let index = 0; index < compact.length; index += size) {
		blocks.push(compact.slice(index, index + size));
	}
	return blocks.join(" ");
}

/** Relie les contrôles HTML au moteur, sans variable globale ni remplacement de window.onload. */
function initializeCeda(form) {
	const control = id => form.querySelector(`#${id}`);
	const error = form.querySelector(".ceda-error");
	const gridCells = form.querySelectorAll("[data-ceda-letter]");
	const original = control("Original_TextArea");
	const encrypted = control("Encrypting_TextArea");
	// Les réglages suivent la dernière zone dans laquelle l’utilisateur a saisi du texte.
	let decrypt = false;

	/** Sélectionne l’alphabet correspondant aux réglages courants. */
	function selectedAlphabet() {
		if (control("TypeCaesar").checked) {
			return getCaesarAlphabet(control("SettingCaesar").valueAsNumber);
		}
		if (control("TypeGridH").checked || control("TypeGridV").checked) {
			return getGridAlphabet(control("SettingGrid").value, control("TypeGridV").checked);
		}
		return PresetAlphabets[control("SettingParticular").value];
	}

	/** Affiche la grille valide ou une erreur, sans écraser les textes saisis. */
	function refreshAlphabet() {
		try {
			const alphabet = selectedAlphabet();
			gridCells.forEach((cell, index) => cell.textContent = alphabet[index]);
			error.hidden = true;
			error.textContent = "";
			return alphabet;
		} catch (exception) {
			gridCells.forEach(cell => cell.textContent = "");
			error.textContent = exception.message;
			error.hidden = false;
			return null;
		}
	}

	/** Affiche les réglages de la méthode active et actualise la grille. */
	function updateMethod() {
		control("SettingCaesarRow").hidden = !control("TypeCaesar").checked;
		control("SettingGridRow").hidden = !(control("TypeGridH").checked || control("TypeGridV").checked);
		control("SettingParticularRow").hidden = !control("TypeParticular").checked;
		transform();
	}

	/** Actualise uniquement la zone opposée, sans modifier la saisie ni sa position de curseur. */
	function transform() {
		const alphabet = refreshAlphabet();
		if (alphabet === null) {
			return;
		}
		const letterCase = control("TypeCasseUpper").checked ? "upper" :
			control("TypeCasseLower").checked ? "lower" :
				control("TypeCasseRandom").checked ? "random" : "unchanged";
		const spacing = control("TypeSpace4").checked ? "blocks4" :
			control("TypeSpace5").checked ? "blocks5" :
				control("TypeSpaceRandom").checked ? "random" : "unchanged";
		const source = decrypt ? encrypted : original;
		const destination = decrypt ? original : encrypted;
		destination.value = formatText(substitute(source.value, alphabet, decrypt), {letterCase, spacing});
	}

	form.addEventListener("submit", event => event.preventDefault());
	for (const id of ["TypeCaesar", "TypeGridH", "TypeGridV", "TypeParticular"]) {
		control(id).addEventListener("change", updateMethod);
	}
	for (const id of ["SettingCaesar", "SettingGrid"]) {
		control(id).addEventListener("input", transform);
	}
	control("SettingParticular").addEventListener("change", transform);
	for (const id of ["TypeCasseNoChange", "TypeCasseUpper", "TypeCasseLower", "TypeCasseRandom",
		"TypeSpaceNoChange", "TypeSpace4", "TypeSpace5", "TypeSpaceRandom"]) {
		control(id).addEventListener("change", transform);
	}
	original.addEventListener("input", () => {
		decrypt = false;
		transform();
	});
	encrypted.addEventListener("input", () => {
		decrypt = true;
		transform();
	});
	updateMethod();
}

if (typeof document !== "undefined") {
	document.querySelectorAll("[data-ceda]").forEach(initializeCeda);
}
