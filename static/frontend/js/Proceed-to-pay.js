
/*------------------show and close modal-submit time ------------------- */
let btnsShowModal = document.querySelector("#submit-time");
let modals = document.querySelector("#modal-submit-time");
let overalyModals = document.querySelector("#modal-submit-time .inner-modal");

    btnsShowModal.addEventListener("click", () => {
    modals.classList.add("active");
  });

  overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });
/*------------------show and close modal-submit time ------------------- */
