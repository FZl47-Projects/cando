// change content pakage main new-education and  new Article

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
// change content pakage main new-education and  new Article



/*------------------show and close modal-new-education ------------------- */
let btnShowModaleducation = document.querySelector("#new-education-btn");
let modalseducation = document.querySelector("#modal-education-pakage");
let overalyModals = document.querySelector("#modal-education-pakage .inner-modal");

btnShowModaleducation.addEventListener("click", () => {
    modalseducation.classList.add("active");
});

overalyModals.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal"){
    modalseducation.classList.remove("active");
  }
});


/*------------------show and close modal-new-education ------------------- */




/*------------------show and close modal-new-Article ------------------- */
let btnShowModalsweet = document.querySelector("#new-Article-btn");
let modalsweet = document.querySelector("#modal-add-Article");
let overalyModal = document.querySelector("#modal-add-Article .inner-modal");

btnShowModalsweet.addEventListener("click", () => {
  modalsweet.classList.add("active");
});

overalyModal.addEventListener("click", (e) => {
  if (e.target.className === "inner-modal"){
    modalsweet.classList.remove("active");
  }
});


/*------------------show and close modal-new-Article ------------------- */

/*------------------on and off desired-package in modal ------------------- */


function validate(){
  var checkbox=document.getElementById("check-input");
  var package_delkhah = document.getElementById("package-delkhah");
  if(checkbox.checked==true)
      {
          var a=document.getElementById("small-circle");
          var b=document.getElementById("circle-bironi");
          a.style.right="9%";
          b.style.backgroundColor="#55BF63";
          package_delkhah.style.display="block";
          // for(var i=0;i<package_delkhah.length;i++)
          // {
          //   package_delkhah[i].style.display="flex";
          // }
         
      }
      else{
          var x=document.getElementById("small-circle");
          var y=document.getElementById("circle-bironi");
          x.style.right="54%";
          y.style.backgroundColor="#9e9fb1";
          package_delkhah.style.display="none";
          
          // for(var i=0;i<package_delkhah.length;i++)
          // {
          //   package_delkhah[i].style.display="none";
          // }
      }
}


/*------------------on and off desired-package in modal ------------------- */


