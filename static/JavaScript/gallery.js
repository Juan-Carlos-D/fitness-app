document.addEventListener('DOMContentLoaded', () => {
    const images = document.querySelectorAll('.gallery-container img');
    const prevButton = document.querySelector('.nav-button.prev');
    const nextButton = document.querySelector('.nav-button.next');

    let currentIndex = 0;

    function showImage(index) {
        images.forEach(img => img.style.display = 'none');
        images[index].style.display = 'block';
    }

    function changeImage(direction) {
        currentIndex = (currentIndex + direction + images.length) % images.length;
        showImage(currentIndex);
    }

    prevButton.addEventListener('click', () => {
        changeImage(-1); // Previous image
    });

    nextButton.addEventListener('click', () => {
        changeImage(1); // Next image
    });

    showImage(currentIndex); // Initial display
});
