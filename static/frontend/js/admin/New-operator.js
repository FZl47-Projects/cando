/*------------------on and off desired-package  ------------------- */
function validate(){
  var checkbox=document.getElementById("check-input");
 // var checkboxs=document.getElementById("check-inputs");
  if(checkbox.checked==true)
      {
          var a=document.getElementById("small-circle");
          var b=document.getElementById("circle-bironi");
          a.style.right="9%";
          b.style.backgroundColor="#55BF63";
        
          // for(var i=0;i<package_delkhah.length;i++)
          // {
          //   package_delkhah[i].style.display="flex";
          // }
         
      }
      else{
          var x=document.getElementById("small-circle");
          var y=document.getElementById("circle-bironi");
          x.style.right="54%";
          y.style.backgroundColor="#9e9fb1";
         
          
          // for(var i=0;i<package_delkhah.length;i++)
          // {
          //   package_delkhah[i].style.display="none";
          // }
      }
      // if(checkboxs.checked==true)
      // {
      //     var as=document.getElementById("small-circles");
      //     var bs=document.getElementById("circle-bironis");
      //     as.style.right="9%";
      //     bs.style.backgroundColor="#55BF63";
        
      //     // for(var i=0;i<package_delkhah.length;i++)
      //     // {
      //     //   package_delkhah[i].style.display="flex";
      //     // }
         
      // }
      // else{
      //     var xs=document.getElementById("small-circles");
      //     var ys=document.getElementById("circle-bironis");
      //     xs.style.right="54%";
      //     ys.style.backgroundColor="#9e9fb1";
         
          
      //     // for(var i=0;i<package_delkhah.length;i++)
      //     // {
      //     //   package_delkhah[i].style.display="none";
      //     // }
      // }
}

/*------------------on and off desired-package  ------------------- */


// change content pakage main new-education and  new Article

let btns = document.querySelectorAll(".btn-change");
let contents = document.querySelectorAll(".Sale-operator-content");

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
// change content pakage main new-education and  new Article