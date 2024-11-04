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




//Dropdown selection in add-catagory form
let dropdown = document.getElementById('dropdownMenu');

function toggleDropdown() {
    let dropdown = document.getElementById('dropdownMenu');
    if (dropdown.style.display === 'block') {
        dropdown.style.display = 'none';
        document.removeEventListener('click', closeDropdownOnClickOutside);
    } else {
        dropdown.style.display = 'block';
        document.addEventListener('click', closeDropdownOnClickOutside);
    }
}

// close dropdown when clicking outside
function closeDropdownOnClickOutside(event) {
    let dropdown = document.getElementById('dropdownMenu');
    let selectedText = document.getElementById('selectedText');
    if (dropdown && dropdown.style.display === 'block' &&
        !dropdown.contains(event.target) && event.target !== selectedText) {
        dropdown.style.display = 'none';
        document.removeEventListener('click', closeDropdownOnClickOutside);
    }
}

function updateSelection() {
    let checkboxes = document.querySelectorAll('input[name="fac"]:checked');
    let selectedText = Array.from(checkboxes).map(checkbox => checkbox.parentElement.textContent.trim());
    let displayText = selectedText.length > 0 ? selectedText.join(', ') : 'เลือกคณะ';
    document.getElementById('selectedText').textContent = displayText;
}

function clearSelection() {
    let checkboxes = document.querySelectorAll('input[name="fac"]');
    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    });
    document.getElementById('selectedText').textContent = 'เลือกคณะ';
}

