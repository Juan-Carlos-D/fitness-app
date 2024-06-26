document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question-title');

    questions.forEach(question => {
        question.addEventListener('click', function() {
            const answer = this.nextElementSibling;
            const icon = this.querySelector('.toggle-icon');

            if (answer.style.display === "none" || answer.style.display === "") {
                answer.style.display = "block";
                icon.innerHTML = '&#9660;'; // Down-facing triangle
            } else {
                answer.style.display = "none";
                icon.innerHTML = '&#9658;'; // Right-facing triangle
            }
        });
    });
});
