// change content  new tickets  and  all tickets 
let btns = document.querySelectorAll(".btn-change");
let contents = document.querySelectorAll(".content-tickets");

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
// change content new tickets  and  all tickets 


/*------------------show and close response-tickets ------------------- */
let btnsShowModal = document.querySelectorAll("#response");
let modals = document.querySelector("#modal-ticket");
let overalyModals = document.querySelector("#modal-ticket .inner-modal");

btnsShowModal.forEach((item,index)=>{
  item.addEventListener("click", () => {
    modals.classList.add("active");
  });
});
overalyModals.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal"){
    modals.classList.remove("active");
  }
});


  //   btnsShowModal.addEventListener("click", () => {
  //   modals.classList.add("active");
  // });

  // overalyModals.addEventListener("click", (e) => {
  //   if (e.target.className === "inner-modal"){
  //     modals.classList.remove("active");
  //   }
  // });
/*------------------show and close response-tickets ------------------- */