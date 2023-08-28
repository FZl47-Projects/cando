let esfang = document.querySelectorAll("#esfang-div");
let esfang_img = document.querySelectorAll("#esfang-img");


let filing = document.querySelectorAll("#filing-div");
let filing_img = document.querySelectorAll("#filing-img");

let cream = document.querySelectorAll("#cream-div");
let cream_img = document.querySelectorAll("#cream-img");

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


let btn_add_image_field = document.querySelector('#btn-add-image-field')
let container_image_fields = document.querySelector('.container-image-fields')
btn_add_image_field.addEventListener('click', function () {
    let cnt_field = document.createElement('div')
    cnt_field.classList.add('container-field-image-additional')
    cnt_field.innerHTML = `
                <input type="file" class="my-1" name="image" id="imgfile" required>
                <i class="btn-delete-image-field fa fa-trash text-danger" style="margin-right: 15px;"></i>
            `
    container_image_fields.appendChild(cnt_field)
    cnt_field.querySelector('.btn-delete-image-field').addEventListener('click', function () {
        this.parentElement.remove()
    })

})

let type_order_select = document.querySelector('#Order')
type_order_select.addEventListener('change', function (e) {
    e = e.target
    let option = e.options[e.selectedIndex]
    let key = option.getAttribute('key')
    if (key == 'pic-on-cake') {
        btn_add_image_field.classList.add('d-none')
        document.querySelectorAll('.container-field-image-additional').forEach(function (el) {
            el.remove()
        })
    } else if (key == 'model') {
        btn_add_image_field.classList.remove('d-none')
    }
})


$('.esfang-div').on('click', function (e) {
    document.querySelector('input[name="taste_spongy"]').value = this.querySelector('.Ntaste').innerText
})

$('.filing-div').on('click', function (e) {
    document.querySelector('input[name="filing_cake"]').value = this.querySelector('.Ntaste').innerText
})

$('.cream-div').on('click', function (e) {
    document.querySelector('input[name="taste_cream"]').value = this.querySelector('.Ntaste').innerText
})