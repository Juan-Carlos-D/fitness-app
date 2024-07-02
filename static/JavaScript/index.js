document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-list");
    const dropdowns = document.querySelectorAll(".dropdown");

    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        navMenu.classList.toggle("active");
    });

    document.querySelectorAll(".nav-link").forEach(link => {
        link.addEventListener("click", (e) => {
            const parentItem = e.target.parentElement;
            
            if (parentItem.classList.contains("dropdown")) {
                e.preventDefault(); // Prevent the default link action
                parentItem.classList.toggle("active");
            } else {
                hamburger.classList.remove("active");
                navMenu.classList.remove("active");
            }
        });
    });

    // Close menu when a non-dropdown nav link is clicked
    document.querySelectorAll(".nav-link:not(.dropdown .nav-link)").forEach(link => {
        link.addEventListener("click", () => {
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
        });
    });

    // Functionality to close the dropdown menu when the parent is clicked again
    dropdowns.forEach(dropdown => {
        dropdown.addEventListener("click", (e) => {
            if (dropdown.classList.contains("active")) {
                e.preventDefault();
                dropdown.classList.remove("active");
            }
        });
    });
});
