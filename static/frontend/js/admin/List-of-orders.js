// change content General-orders and  showcase of the day

let btns = document.querySelectorAll(".btn-change");
let contents = document.querySelectorAll(".content-price");

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
// change content General-orders and  showcase of the day