const menuIcon = document.getElementById('menu-icon');
const navLink = document.getElementById('nav-links');
const menuImg = document.getElementById('menu-img')

menuIcon.addEventListener('click', function(event) {
    event.preventDefault();
    navLink.classList.toggle('show');

    if (navLink.classList.contains('show')) {
        menuImg.src = "../static/icon/close.png";
        menuImg.classList.add('rotate');
    } 
    else {
        menuImg.src = "../static/icon/menu.png";
        menuImg.classList.remove('rotate');
    }
    event.stopPropagation();
});

document.addEventListener('click', function(event) {
    if (!navLink.contains(event.target) && !menuIcon.contains(event.target)) {
        navLink.classList.remove('show');
        menuImg.src = "../static/icon/menu.png";
        menuImg.classList.remove('rotate');
    }
});

const overlay = document.getElementById('popup');

overlay.addEventListener('click', function(event) {
    if (event.target === overlay) {
        window.location.hash = '';
    }
});



//Upload picture in Register form
const fileInput = document.getElementById("fileInput");
const uploadImage = document.getElementById("uploadImage");

uploadImage.addEventListener("click", () => {
    fileInput.click();
});


fileInput.addEventListener("change", (event) => {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            uploadImage.src = e.target.result;
        };
        reader.readAsDataURL(file);
    }
});