const cards = document.querySelectorAll("section.standard-room-card");
const flipButtons = document.querySelectorAll(".flip-back-link > a");
const flip = document.querySelectorAll(".flipper");
const cardButtons = document.querySelectorAll(".standard-room-link");

for (let i = 0; i < cards.length; i++) {
	cardButtons[i].addEventListener("click", () => {
		flip[i].classList.add("active");
	});

	flipButtons[i].addEventListener("click", () => {
		flip[i].classList.remove("active");
	})
}

