// change content Sales operator  and cake operator

let btns = document.querySelectorAll(".btn-change");
let contents = document.querySelectorAll(".Sales-operator");

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
// change content Sales operator  and cake operator

/*------------------show and close Sales operator ------------------- */
let btnsShowModal = document.querySelector("#btn-send-notificationz");
let modals = document.querySelector("#modal-send-notification");
let overalyModals = document.querySelector("#modal-send-notification .inner-modal");

    btnsShowModal.addEventListener("click", () => {
    modals.classList.add("active");
  });

  overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });
/*------------------show and close Sales operator ------------------- */





/*------------------show and close modal cake operator------------------- */
let btnShowModal = document.querySelector("#general-notification");
let modal = document.querySelector("#modal-General-notification");
let overalyModal = document.querySelector("#modal-General-notification .inner-modal");

    btnShowModal.addEventListener("click", () => {
    modal.classList.add("active");
  });

  overalyModal.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modal.classList.remove("active");
    }
  });
/*------------------show and close modal cake operator------------------- */