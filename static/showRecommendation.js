var n = 0;
window.ev = false;
document.getElementById("carousel-inner").onmouseenter = function () {
  window.ev = true;
};
document.getElementById("carousel-inner").onmouseleave = function () {
  window.ev = false;
  setTimeout(autoSlide, 400);
};

function autoSlide() {
  if (window.ev == false) {
    n++;
    if (n === 5) n = 1;
    document.getElementById("carousel-" + n).checked = true;
    setTimeout(autoSlide, 4000);
  }
}
autoSlide();

// const sliderWrap = document.querySelector(".carousel-inner");
// const sliderSize = document.querySelector(".carousel-item").clientWidth;
// const sliderLeftBtn = document.querySelector(".carousel_left_btn");
// const sliderRightBtn = document.querySelector(".carousel_right_btn");
// let currentNum = 1;
// let position = 0;

// sliderLeftBtn.addEventListener("click", () => {
//   if (currentNum <= 1) return;
//   position += sliderSize;
//   sliderWrap.style.transform = `translateX(${position}px)`;
//   currentNum -= 1;
// });

// sliderRightBtn.addEventListener("click", () => {
//   if (currentNum >= 4) return;
//   position -= sliderSize;
//   sliderWrap.style.transform = `translateX(${position}px)`;
//   currentNum += 1;
// });