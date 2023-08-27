
  let backBtn = document.querySelector(".back");
  backBtn.addEventListener("click", () => {
    backPage();
  });
  
  
  const backPage = () => {
      history.back();
    };