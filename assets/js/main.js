const fixHeader = document.querySelector('.header-wrapper');

const body = document.querySelector('body');


window.addEventListener("scroll", () => {
	if (window.pageYOffset < 100) {
		fixHeader.style.background = "red";
		fixHeader.innerHTML = "hey"
	}
});

console.log(body.scrollTop);