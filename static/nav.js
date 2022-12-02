const togglebtn = document.querySelector('.navbar-togglebtn');
const menu = document.querySelector('.navbar-menu');

togglebtn.addEventListener('click', clicktoggle);

function clicktoggle() {
    menu.classList.toggle('active');
}