
let form = document.querySelector(".form-login");
let phoneNumber = document.querySelector("#phoneNumber-login");
let password = document.querySelector("#password-login");

phoneNumber.focus();

// submit form
form.addEventListener("submit", async (e) => {
  e.preventDefault();
  checkInput();
  if (checkInput() === false) {
    let userLogin = {
      phonenumber: `${phoneNumber.value}`,
      password: `${password.value}`,
    };

    const result = await login(userLogin);

    if (result === false || result === "" || result === undefined) {
      successAlert("error", "کاربر یافت نشد");
    }
    else{
      window.localStorage.setItem("user" , result)

      setTimeout(() => {

        window.location.replace("./index.html");
      }, 2000);
    }
  }
});

// validation inputs
const checkInput = () => {
  const phoneValue = phoneNumber.value.trim();
  const passwordValue = password.value.trim();
  let errors = {};
  if (phoneValue === "") {
    setError(phoneNumber, "لطفا شماره موبایل خود را وارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (!!checkPhoneNumber(`${phoneValue}`) === false) {
    setError(phoneNumber, "لطفا شماره موبایل معتبر وارد کنید");
    errors.phoneNumber = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(phoneNumber);
    delete errors.phoneNumber;
  }

  if (passwordValue === "") {
    setError(password, "لطفا رمز عبور خود را وارد کنید");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else if (passwordValue.length < 2) {
    setError(password, "رمز عبور نباید کمتر از هشت کاراکتر باشد");
    errors.password = "لطفا نام و نام خانوادگی خود را وارد کنید";
  } else {
    setSuccess(password);
    delete errors.password;
  }

  return !!Object.keys(errors).length;
};









// set errors
const setError = (input, message) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");

  formGroup.classList.add("error");
  small.innerText = message;
};

// set success
const setSuccess = (input) => {
  const formGroup = input.parentElement;
  const contentFormGroup = formGroup.parentElement;
  const small = contentFormGroup.querySelector("small");
  formGroup.classList.add("success");
  small.innerText = "";
};
