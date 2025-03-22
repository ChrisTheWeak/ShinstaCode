document.querySelectorAll(".copy").forEach(copyButton => {
	copyButton.addEventListener("click", () => {
		const targetElement = document.querySelector(copyButton.dataset.copy);
		const textToCopy = targetElement.textContent;
		console.log(targetElement);
		navigator.clipboard.writeText(textToCopy)
	})
})