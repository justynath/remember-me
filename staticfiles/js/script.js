
document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.card-excerpt').forEach((excerpt) => {
        const button = excerpt.nextElementSibling;

        if (excerpt.scrollHeight > excerpt.offsetHeight) {
            button.style.display = 'block';
        }

        button.addEventListener('click', () => {
            excerpt.classList.toggle('expanded');

            if (excerpt.classList.contains('expanded')) {
                button.textContent = 'Show Less';
            } else {
                button.textContent = 'Show More';
            }
        });
    });
});


