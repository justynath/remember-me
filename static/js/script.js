document.querySelectorAll('.card-excerpt').forEach((excerpt) => {
    const button = excerpt.nextElementSibling; // The Show More button

    // Check if the content overflows
    if (excerpt.scrollHeight > excerpt.offsetHeight) {
        button.style.display = 'block'; // Show the button if truncated
    }

    button.addEventListener('click', () => {
        // Toggle the 'expanded' class on the text
        excerpt.classList.toggle('expanded');

        // Update button text based on state
        if (excerpt.classList.contains('expanded')) {
            button.textContent = 'Show Less';
        } else {
            button.textContent = 'Show More';
        }
    });
});
