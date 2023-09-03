// change content pakage active-orders and Previous-orders

let btns = document.querySelectorAll(".btn-orders");
let contents = document.querySelectorAll(".order");

try {
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
} catch (e) {
}
// change content pakage active-orders and Previous-orders


/*------------------show and close modal Order details ------------------- */
let btnsShowModal = document.querySelectorAll("#order-content");
let modals = document.querySelector("#modal-Order-details");
let overalyModals = document.querySelector("#modal-Order-details .inner-modal");

//   btnsShowModal.addEventListener("click", () => {
//   modals.classList.add("active");
// });

// overalyModals.addEventListener("click", (e) => {
//   if (e.target.className === "inner-modal"){
//     modals.classList.remove("active");
//   }
// });

btnsShowModal.forEach((item, index) => {
    item.addEventListener("click", () => {

        modals.classList.add("active");
    });
});
overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal") {
        modals.classList.remove("active");
    }
});
/*------------------show and close modal Order details------------------- */


/*------------------on and off desired-package in modal ------------------- */


function validate() {
    var checkbox = document.getElementById("check-input");
    if (checkbox.checked == true) {
        var a = document.getElementById("small-circle");
        var b = document.getElementById("circle-bironi");
        var text = document.getElementById("text-etebar");
        var text1 = document.getElementById("texts-etebar");


        a.style.right = "9%";
        b.style.backgroundColor = "#55BF63";
        text.style.color = "#55BF63";
        text1.style.color = "#55BF63";

    } else {
        var x = document.getElementById("small-circle");
        var y = document.getElementById("circle-bironi");
        var z = document.getElementById("text-etebar");
        var z1 = document.getElementById("texts-etebar");

        x.style.right = "54%";
        y.style.backgroundColor = "#9e9fb1";
        z.style.color = "black";
        z1.style.color = "black";

    }
}


/*------------------on and off desired-package in modal ------------------- */