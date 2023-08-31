/*------------------show and close modal-submit time ------------------- */
let btnsShowModal = document.querySelector("#submit-time");
let modals = document.querySelector("#modal-submit-time");
let overalyModals = document.querySelector("#modal-submit-time .inner-modal");

// btnsShowModal.addEventListener("click", () => {
//     modals.classList.add("active");
// });
//
// overalyModals.addEventListener("click", (e) => {
//     if (e.target.className === "inner-modal") {
//         modals.classList.remove("active");
//     }
// });
/*------------------show and close modal-submit time ------------------- */


var toggle = document.getElementById("container");
var toggleContainer = document.getElementById("toggle-container");
const toggleContent1 = document.getElementById("page-one");
const toggleContent2 = document.getElementById("page-two");
var toggleNumber;

toggle.addEventListener("click", function () {
    toggleNumber = !toggleNumber;
    if (toggleNumber) {
        toggleContainer.style.clipPath = "inset(0 0 0 50%)";
        toggleContainer.style.backgroundColor = "#D74046";
        toggleContent1.style.transform = "translateX(100%)";
        toggleContent2.style.transform = "translateX(0%)";
    } else {
        toggleContainer.style.clipPath = "inset(0 50% 0 0)";
        toggleContainer.style.backgroundColor = "dodgerblue";
        toggleContent2.style.transform = "translateX(-100%)";
        toggleContent1.style.transform = "translateX(0%)";
    }
});