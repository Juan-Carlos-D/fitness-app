document.addEventListener("DOMContentLoaded", function() {
    const hamburger = document.querySelector(".hamburger");
    const navMenu = document.querySelector(".nav-list");
    const dropdowns = document.querySelectorAll(".dropdown");

    hamburger.addEventListener("click", () => {
        hamburger.classList.toggle("active");
        navMenu.classList.toggle("active");
    });

    document.querySelectorAll(".dropdown > .nav-link").forEach(link => {
        link.addEventListener("click", (e) => {
            e.preventDefault(); // Prevent the default link action
            const parentItem = link.parentElement;
            const dropdownMenu = parentItem.querySelector(".dropdown-menu");

            if (parentItem.classList.contains("active")) {
                parentItem.classList.remove("active");
                dropdownMenu.style.display = "none";
            } else {
                // Close other open dropdowns
                document.querySelectorAll(".dropdown.active").forEach(openDropdown => {
                    openDropdown.classList.remove("active");
                    openDropdown.querySelector(".dropdown-menu").style.display = "none";
                });

                // Open the clicked dropdown
                parentItem.classList.add("active");
                dropdownMenu.style.display = "block";
            }
        });
    });

    // Close menu when a non-dropdown nav link is clicked
    document.querySelectorAll(".nav-link:not(.dropdown .nav-link)").forEach(link => {
        link.addEventListener("click", () => {
            hamburger.classList.remove("active");
            navMenu.classList.remove("active");
            // Close any open dropdowns
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove("active");
                dropdown.querySelector(".dropdown-menu").style.display = "none";
            });
        });
    });
});

