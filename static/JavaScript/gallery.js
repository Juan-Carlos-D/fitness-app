// document.addEventListener('DOMContentLoaded', () => {
//     const images = document.querySelectorAll('.gallery-container img');
//     const prevButton = document.querySelector('.nav-button.prev');
//     const nextButton = document.querySelector('.nav-button.next');

//     let currentIndex = 0;

//     function showImage(index) {
//         images.forEach(img => img.style.display = 'none');
//         images[index].style.display = 'block';
//     }

//     function changeImage(direction) {
//         currentIndex = (currentIndex + direction + images.length) % images.length;
//         showImage(currentIndex);
//     }

//     prevButton.addEventListener('click', () => {
//         changeImage(-1);

//     nextButton.addEventListener('click', () => {
//         changeImage(1); 
//     });

//     showImage(currentIndex); 
// });


var counter = 1;
setInterval(function() {
    document.getElementById('radio' + counter).checked = true;
    counter++;
    if(counter > 4) {
        counter = 1;
    }
}, 5000);