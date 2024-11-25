const menuToggle = document.getElementById("menuToggle");
const offcanvasNav = document.getElementById("offcanvasNav");

menuToggle.addEventListener("click", () => {
    menuToggle.classList.toggle("active");
    offcanvasNav.classList.toggle("active");
});
