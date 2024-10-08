const menuIcon = document.getElementById('menu-icon');
const menuImg = document.getElementById('menu-img');
const navLinks = document.getElementById('nav-links');
menuIcon.addEventListener('click', function() {
    if (navLinks.classList.contains('show')) {
        navLinks.classList.remove('show');
        menuImg.src = "../static/icon/menu.png";
        menuImg.classList.remove('rotate');
    } else {
        navLinks.classList.add('show');
        menuImg.src = "../static/icon/close.png";
        menuImg.classList.add('rotate');
    }
});
