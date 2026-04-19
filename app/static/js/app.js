const mode_switch = document.getElementById("mode_switch")
const root = document.documentElement

let dark_mode = false

function update_theme() {
	const theme = root.getAttribute("data-theme") || "light";
	const is_dark = theme === "dark";

	mode_switch.textContent = is_dark ? "[ ☾ ]" : "[ ☼ ]";

	document.querySelectorAll("[data-theme-image]").forEach((img) => {
		img.src = is_dark ? img.dataset.darkSrc : img.dataset.lightSrc;
	});
}

mode_switch?.addEventListener("click", () => {
	const currentTheme = root.getAttribute("data-theme") || "light";
	const newTheme = currentTheme === "dark" ? "light" : "dark";

	root.setAttribute("data-theme", newTheme);
	localStorage.setItem("theme", newTheme);
	update_theme();
})

const saved_theme = localStorage.getItem("theme");
if (saved_theme) {
	root.setAttribute("data-theme", saved_theme);
}

update_theme();
