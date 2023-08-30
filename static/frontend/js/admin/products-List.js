/*------------------show and close modal products list ------------------- */
let btnsShowModal = document.querySelectorAll("#new-cake-btn");
let modals = document.querySelectorAll("#modal-products-list");
let overalyModals = document.querySelectorAll("#modal-products-list .inner-modal");

btnsShowModal.forEach((item, index) => {
    item.addEventListener("click", () => {

        modals[0].classList.add("active");
    });
});
overalyModals.forEach((item, index) => {

    item.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal") {
            modals[0].classList.remove("active");
        }
    });
})

/*------------------show and close modal products list------------------- */


// change content main with menu

let btns = document.querySelectorAll(".sweet");
let contents = document.querySelectorAll(".content-pakage");

btns.forEach((item, index) => {
    item.addEventListener("click", () => {
        btns.forEach((item) => {
            item.classList.remove("active");

        });
        contents.forEach((item) => {
            item.classList.remove("active");
        });
        btns[index].classList.add("active");
        contents[index].classList.add("active");
    });
});
// change content pakage main new-birth and  new sweet

let btnseditModal = document.querySelectorAll(".cart-image-edit");
let modalseditproduct = document.querySelectorAll(".product-edit-modal");
let overalyModalseditproduct = document.querySelectorAll("#product-edit-modal .inner-modal");

btnseditModal.forEach((item, index) => {
    item.addEventListener("click", () => {
        modalseditproduct[index].classList.add("active");
    });
});
overalyModalseditproduct.forEach((item, index) => {
    item.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal") {
            modalseditproduct[index].classList.remove("active");
        }
    });
})
