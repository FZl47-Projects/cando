//swiper filing
const swiper_filing = new Swiper('#myswiper', {
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
            slidesPerView: 3,
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
            slidesPerView: 3,
        }
    },

    // Navigation arrows
    navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
    },


})
//swiper filing

//swiper filing
// const swiper_esfanje = new Swiper('#myswiper-esfanje', {
//     // Default parameters
//     slidesPerView: 4,
//     spaceBetween: 10,
//     // Responsive breakpoints

//     autoplay: {
//         delay: 4000
//     },


//     breakpoints: {
//         // when window width is >= 320px
//         200: {
//             slidesPerView: 3,
//         },
//         // when window width is >= 480px
//         500: {
//             slidesPerView: 3,
//         },
//         // when window width is >= 640px
//         768: {
//             slidesPerView: 3,
//         },
//         992: {
//             slidesPerView: 3,
//         }
//     },

//     // Navigation arrows
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },


// })
//swiper filing



//swiper filing
// const swiper_cream = new Swiper('#myswiper-cream', {
//     // Default parameters
//     slidesPerView: 4,
//     spaceBetween: 10,
//     // Responsive breakpoints

//     autoplay: {
//         delay: 4000
//     },


//     breakpoints: {
//         // when window width is >= 320px
//         200: {
//             slidesPerView: 3,
//         },
//         // when window width is >= 480px
//         500: {
//             slidesPerView: 3,
//         },
//         // when window width is >= 640px
//         768: {
//             slidesPerView: 3,
//         },
//         992: {
//             slidesPerView: 3,
//         }
//     },

//     // Navigation arrows
//     navigation: {
//         nextEl: '.swiper-button-next',
//         prevEl: '.swiper-button-prev',
//     },


// })
//swiper filing


let btns = document.querySelectorAll(".top-arrows");
let contents = document.querySelectorAll("#myswiper");


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