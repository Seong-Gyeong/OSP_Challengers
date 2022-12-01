const dropDownSection = document.querySelector(".second");
const dropDownBtn = document.querySelector(".second_btn");
const dropDownMenu = document.querySelector(".second_dropdown");

const options = document.querySelectorAll(".second_dropdown_option");

dropDownBtn.addEventListener("click", () => {
  dropDownMenu.classList.toggle("show");
});

options.forEach((option) => {
  option.addEventListener("click", (event) => {
    // dropDownBtn.firstChild.data = event.currentTarget.innerText;
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
