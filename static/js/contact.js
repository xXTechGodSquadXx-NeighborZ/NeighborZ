setTimeout(() => {
	document.querySelector("select").classList.add("has-placeholder");
	document.querySelector("select").options[0].disabled = true;

	document.querySelector("select").addEventListener("change", e => {
		e.currentTarget.classList.remove("has-placeholder");
	});
}, 100);
