/*------------------show and close modal-hamberger ------------------- */

let btnHamburger = document.querySelector("#hamburger");
let menuMobile = document.querySelector(".menu-admin");
let closeMenu = document.querySelector(".overlay-menu-mobile");

btnHamburger.addEventListener("click", () => {
    menuMobile.classList.add("active");
});
closeMenu.addEventListener("click", () => {
    menuMobile.classList.remove("active");
});

/*------------------show and close modal-hamberger ------------------- */


//swiper
var swiper = new Swiper(".mySwiper", {
    effect: "coverflow",
    grabCursor: true,
    centeredSlides: true,
    slidesPerView: "auto",
    coverflowEffect: {
        rotate: 0,
        stretch: 0,
        depth: 100,
        modifier: 2,
        slideShadows: true,
    },
    breakpoints: {
        360: {
            slidesPerView: 3,
        },
        600: {
            slidesPerView: 3,
        },
        700: {
            slidesPerView: 4,
        },
        992: {
            slidesPerView: 4,
        },
        1200: {
            slidesPerView: 4,
        },
    },
    pagination: {
        el: ".swiper-pagination",
    },
    pagination: {
        el: '.swiper-pagination',
        clickable: true,
    },

    autoplay: {
        delay: 2000,
    },

});


//swiper
const products = new Swiper('#slider-offer', {
    // Optional parameters
    direction: 'horizontal',

    spaceBetween: 10,
    slidesPerView: 1,

    // If we need pagination
    breakpoints: {
        // when window width is >= 320px
        320: {
            slidesPerView: 3,
        },
        // when window width is >= 480px
        500: {
            slidesPerView: 4,
        },
        // when window width is >= 640px
        768: {
            slidesPerView: 4,
        },
        992: {
            slidesPerView: 6,
        }

    },
    autoplay: {
        delay: 2000,
    },
    loop: true,

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },

    // And if we need scrollbar
    scrollbar: {
        el: '.swiper-scrollbar',
    },
});


///کلیک کردن روی عکس ها و محتوای ها عکس رو نمایش دادن
let btns = document.querySelectorAll("#image-product");
let contents = document.querySelectorAll(" #new-product");


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


//کلیک کردن روی عکس های اسلایدر و پاپ اپ باز شدن
let slider = document.querySelectorAll(".test2");
let modal_vitrin = document.querySelectorAll(" #modal-edit-showcase");
let overalyModals = document.querySelectorAll("#modal-edit-showcase .inner-modal");

slider.forEach((item, index) => {
    item.addEventListener("click", () => {
        console.log(slider);
        console.log(index);
        modal_vitrin[index].classList.add("active");
    });

});
overalyModals.forEach((item, index) => {

    item.addEventListener("click", (e) => {
        if (e.target.className === "inner-modal") {
            modal_vitrin[index].classList.remove("active");
        }
    });
})

/*------------------exit menu-admin ------------------- */
let exit = document.getElementById("exit");
let menu = document.querySelector(".menu-admin");
exit.addEventListener("click", (e) => {
    menu.classList.remove("active");
})
/*------------------exit menu-admin ------------------- */


// ---

let btns_change_category = document.querySelectorAll(".btn-change-category");
let categories_container = document.querySelectorAll(".category-container");

btns_change_category.forEach((item, index) => {
    item.addEventListener("click", () => {
        btns_change_category.forEach((item) => {
            item.classList.remove("active");
        });
        categories_container.forEach((item) => {
            item.classList.remove("active");
        });
        btns_change_category[index].classList.add("active");
        categories_container[index].classList.add("active");

        // active default item
        try {
            categories_container[index].querySelector('.products-item').click()
        } catch (e) {
        }
    });
});
