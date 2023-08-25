let esfang = document.querySelectorAll("#esfang-div");
let esfang_img = document.querySelectorAll("#esfang-img");


let filing = document.querySelectorAll("#filing-div");
let filing_img = document.querySelectorAll("#filing-img");

let cream = document.querySelectorAll("#cream-div");
let cream_img  = document.querySelectorAll("#cream-img");

esfang.forEach((item, index) => {
  item.addEventListener("click", () => {
    esfang.forEach((item) => {
      item.classList.remove("active");

    });
    esfang_img.forEach((item) => {
      item.classList.remove("active");
    });
    esfang[index].classList.add("active");
    esfang_img[index].classList.add("active");
  });
});
filing.forEach((item, index) => {
    item.addEventListener("click", () => {
        filing.forEach((item) => {
        item.classList.remove("active");
  
      });
      filing_img.forEach((item) => {
        item.classList.remove("active");
      });
      filing[index].classList.add("active");
      filing_img[index].classList.add("active");
    });
  });
  cream.forEach((item, index) => {
    item.addEventListener("click", () => {
        cream.forEach((item) => {
        item.classList.remove("active");
  
      });
      cream_img.forEach((item) => {
        item.classList.remove("active");
      });
      cream[index].classList.add("active");
      cream_img[index].classList.add("active");
    });
  });