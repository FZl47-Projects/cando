
/*------------------show and close modal-instruction ------------------- */
let btnsShowModal = document.querySelector("#maghale");
let modals = document.querySelector("#modal-instruction");
let overalyModals = document.querySelector("#modal-instruction .inner-modal");

    btnsShowModal.addEventListener("click", () => {
    modals.classList.add("active");
  });

  overalyModals.addEventListener("click", (e) => {
    if (e.target.className === "inner-modal"){
      modals.classList.remove("active");
    }
  });
/*------------------show and close modal-instruction ------------------- */





/*------------------------------Render Page--------------------------------- */

let btnHamburger = document.querySelector(".menu-admin-two");

btnHamburger.addEventListener("click", () => {
  btnHamburger.classList.toggle("active");
});



/*------------------show and close modal-adamtaeid ------------------- */

/*-------------START SLIDER FOR PRODUCTS--------------*/

const swiperProduct = new Swiper('#slider-product', {
    // Default parameters
    slidesPerView: 4,
    spaceBetween: 10,
    // Responsive breakpoints

    // autoplay: {
    //     delay: 4000
    // },


    breakpoints: {
        // when window width is >= 320px
        200: {
            slidesPerView: 1,
        },
        // when window width is >= 480px
        500: {
            slidesPerView: 2,
        },
        // when window width is >= 640px
        768: {
            slidesPerView: 3,
        },
        992: {
            slidesPerView: 4,
        }
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },


})


/*-------------END SLIDER FOR PRODUCTS--------------*/
const swiper = new Swiper('#slider-main', {
    // Default parameters
    slidesPerView: 4,
    spaceBetween: 10,
    // Responsive breakpoints

    autoplay: {
        delay: 4000
    },


    breakpoints: {
        // when window width is >= 320px
        200: {
            slidesPerView: 2,
        },
        // when window width is >= 480px
        500: {
            slidesPerView: 3,
        },
        // when window width is >= 640px
        768: {
            slidesPerView: 3,
        },
        992: {
            slidesPerView: 5,
        }
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },


})

const swipeammozesh = new Swiper('#slider-amoozeshsavarkari', {
    // Default parameters
    slidesPerView: 1,
    spaceBetween: 10,
    // Responsive breakpoints

    autoplay: {
        delay: 2000
    },

    pagination: {
        el: '.swiper-pagination',
        clickable: true
    },


})