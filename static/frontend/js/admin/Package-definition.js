// change content pakage main new-birth and  new sweet

let btns = document.querySelectorAll(".btn-change");
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

/*------------------show and close modal-new-birth ------------------- */
let btnsShowModal = document.querySelector("#new-birth-btn");
let modals = document.querySelector("#modal-newbirth-pakage");
let overalyModals = document.querySelector("#modal-newbirth-pakage .inner-modal");

    btnsShowModal.addEventListener("click", () => {
    modals.classList.add("active");
  });

  overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });
/*------------------show and close modal-new-birth ------------------- */

/*------------------show and close modal-new-sweet ------------------- */
  let btnShowModalsweet = document.querySelector("#new-sweet-btn");
  let modalsweet = document.querySelector("#modal-making-sweets");
  let overalyModal = document.querySelector("#modal-making-sweets .inner-modal");
  
  btnShowModalsweet.addEventListener("click", () => {
    modalsweet.classList.add("active");
  });

  overalyModal.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modalsweet.classList.remove("active");
    }
  });


/*------------------show and close modal-new-sweet ------------------- */