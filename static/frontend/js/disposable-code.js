// import Auxiliary functions
import { checkPhoneNumber } from './services.js';



let form = document.querySelector(".form-disposable-code");
let formConfirm = document.querySelector(".form-confirm-code");
let phoneNumber = document.querySelector("#numberPhone");
let codeConfirm = document.querySelector("#code");
let timing = 60;
let btnTimer = document.querySelector("#btn-timer")
let timingHmtl = document.querySelector("#time")



function setTime() {

    if (timing == 0) {
        btnTimer.removeAttribute("disabled");
        timingHmtl.classList.add("d-none")
        btnTimer.classList.add("active")
        // clearInterval(timer)
    };
    //   let h = Math.floor(timing / 3600);
    let m = Math.floor((timing % 3600) / 60);
    let s = (timing % 3600) % 60;
    s = s < 10 ? "0" + s : s;
    //   document.querySelector(".hour").innerHTML = h;
    document.querySelector("#minute").innerHTML = `0${m}`;
    document.querySelector("#second").innerHTML = s;
}

let timer = setInterval(() => {
    timing -= 1;
    setTime();
}, 1000);

const startTimer = () => {
    timer = setInterval(() => {
        timing -= 1;
        setTime();
    }, 1000)
}

clearInterval(timer)
phoneNumber.focus();




// submit form
form.addEventListener("submit", (e) => {
    e.preventDefault();
    checkInput("phone")

    if (checkInput("phone") === false) {
        // successAlert("عملیات با موفقیت انجام شد")


        form.classList.remove("active");
        formConfirm.classList.add("active");

        startTimer()



    }
})

formConfirm.addEventListener("submit", (e) => {
    e.preventDefault();
    checkInput("code")
    if (checkInput("code") === false) {
        localStorage.setItem("phoneNumber" , phoneNumber.value)

        // successAlert("عملیات با موفقیت انجام شد");

        window.location.replace("./Register.html");
    }
})

// validation inputs
const checkInput = (type) => {
    if (type === 'phone') {
        const phoneNumberValue = phoneNumber.value.trim();
        let errors = {}
        if (phoneNumberValue === "") {
            setError(phoneNumber, "لطفا شماره همراه خود را وارد کنید")
            errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
        } else if (!!checkPhoneNumber(`${phoneNumberValue}`) === false) {
            setError(phoneNumber, "لطفا شماره همراه معتبروارد کنید")
            errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
        } else {
            setSuccess(phoneNumber)
            delete errors.phoneNumber;
        }
        return !!Object.keys(errors).length
    } else {
        const codeVlaue = codeConfirm.value.trim();
        let errors = {}
        if (codeVlaue === "") {
            setError(codeConfirm, "لطفا کد تایید  خود را وارد کنید")
            errors.codeConfirm = "لطفا نام و نام خانوادگی خود را وارد کنید";
        } else if (codeVlaue.length < 4) {
            setError(codeConfirm, "لطفا  کد را کامل وارد کنید")
            errors.codeConfirm = "لطفا نام و نام خانوادگی خود را وارد کنید";
        } else {
            setSuccess(codeConfirm)
            delete errors.codeConfirm;
        }
        return !!Object.keys(errors).length
    }
}

// set errors
const setError = (input, message) => {
    const formGroup = input.parentElement;
    const contentFormGroup = formGroup.parentElement;
    const small = contentFormGroup.querySelector("small");

    formGroup.classList.add("error");
    small.innerText = message;
}

// set success
const setSuccess = (input) => {
    const formGroup = input.parentElement;
    const contentFormGroup = formGroup.parentElement;
    const small = contentFormGroup.querySelector("small");
    formGroup.classList.add("success");
    small.innerText = ""
}


//دکمه ارسال مجدد
let btnResend = document.querySelector("#btn-timer");
btnResend.addEventListener("click", () => {
    form.classList.add("active");
    formConfirm.classList.remove("active")

})