// document.addEventListener("DOMContentLoaded", function() {
//     const hamburger = document.querySelector(".hamburger");
//     const navMenu = document.querySelector(".nav-list");
//     const dropdowns = document.querySelectorAll(".dropdown");

//     hamburger.addEventListener("click", () => {
//         hamburger.classList.toggle("active");
//         navMenu.classList.toggle("active");
//     });

//     document.querySelectorAll(".dropdown > .nav-link").forEach(link => {
//         link.addEventListener("click", (e) => {
//             e.preventDefault(); 
//             const parentItem = link.parentElement;
//             const dropdownMenu = parentItem.querySelector(".dropdown-menu");

//             if (parentItem.classList.contains("active")) {
//                 parentItem.classList.remove("active");
//                 dropdownMenu.style.display = "none";
//             } else {
         
//                 document.querySelectorAll(".dropdown.active").forEach(openDropdown => {
//                     openDropdown.classList.remove("active");
//                     openDropdown.querySelector(".dropdown-menu").style.display = "none";
//                 });

        
//                 parentItem.classList.add("active");
//                 dropdownMenu.style.display = "block";
//             }
//         });
//     });

 
//     document.querySelectorAll(".nav-link:not(.dropdown .nav-link)").forEach(link => {
//         link.addEventListener("click", () => {
//             hamburger.classList.remove("active");
//             navMenu.classList.remove("active");

//             dropdowns.forEach(dropdown => {
//                 dropdown.classList.remove("active");
//                 dropdown.querySelector(".dropdown-menu").style.display = "none";
//             });
//         });
//     });
// });

/*=============== SHOW MENU ===============*/
const showMenu = (toggleId, navId) =>{
    const toggle = document.getElementById(toggleId),
          nav = document.getElementById(navId)
 
    toggle.addEventListener('click', () =>{
        // Add show-menu class to nav menu
        nav.classList.toggle('show-menu')
 
        // Add show-icon to show and hide the menu icon
        toggle.classList.toggle('show-icon')
    })
 }
 
 showMenu('nav-toggle','nav-menu')