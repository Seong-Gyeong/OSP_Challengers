const dropDownSection = document.querySelector(".category");
const dropDownBtn = document.querySelector(".category_btn");
const dropDownMenu = document.querySelector(".category_dropdown");

const dropDownSection2 = document.querySelector(".parking");
const dropDownBtn2 = document.querySelector(".parking_btn");
const dropDownMenu2 = document.querySelector(".parking_dropdown");

const dropDownSection3 = document.querySelector(".price");
const dropDownBtn3 = document.querySelector(".price_btn");
const dropDownMenu3 = document.querySelector(".price_dropdown");

const options = document.querySelectorAll(".category_dropdown_option");
const options2 = document.querySelectorAll(".parking_dropdown_option");
const options3 = document.querySelectorAll(".price_dropdown_option");

dropDownBtn.addEventListener("click", () => {
  dropDownMenu.classList.toggle("show");
});

dropDownBtn2.addEventListener("click", () => {
  dropDownMenu2.classList.toggle("show");
});

dropDownBtn3.addEventListener("click", () => {
  dropDownMenu3.classList.toggle("show");
});

options.forEach((option) => {
  option.addEventListener("click", (event) => {
    dropDownBtn.firstChild.data = event.currentTarget.textContent.trim();
    event.currentTarget.classList.add("selected");
    dropDownMenu.classList.remove("show");

    for (let opt of options) {
      if (opt !== event.currentTarget) {
        opt.classList.remove("selected");
      }
    }
  });
});

options2.forEach((option) => {
  option.addEventListener("click", (event) => {
    dropDownBtn2.firstChild.data = event.currentTarget.textContent.trim();
    event.currentTarget.classList.add("selected");
    dropDownMenu2.classList.remove("show");

    for (let opt of options2) {
      if (opt !== event.currentTarget) {
        opt.classList.remove("selected");
      }
    }
  });
});

options3.forEach((option) => {
  option.addEventListener("click", (event) => {
    dropDownBtn3.firstChild.data = event.currentTarget.textContent.trim();
    event.currentTarget.classList.add("selected");
    dropDownMenu3.classList.remove("show");

    for (let opt of options3) {
      if (opt !== event.currentTarget) {
        opt.classList.remove("selected");
      }
    }
  });
});
