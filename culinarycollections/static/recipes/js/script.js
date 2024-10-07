<script>
    document.addEventListener('DOMContentLoaded', function() {
        const dropdowns = document.querySelectorAll('.dropdown-toggle');

        dropdowns.forEach(dropdown => {
            dropdown.addEventListener('click', function(event) {
                event.preventDefault(); // Prevent default anchor behavior
                const menu = this.nextElementSibling; // Get the dropdown menu
                
                // Toggle the dropdown menu visibility
                if (menu.style.display === "block") {
                    menu.style.display = "none";
                } else {
                    menu.style.display = "block";
                }
            });
        });

        // Close dropdowns if clicked outside
        window.addEventListener('click', function(event) {
            if (!event.target.matches('.dropdown-toggle')) {
                dropdowns.forEach(dropdown => {
                    const menu = dropdown.nextElementSibling;
                    if (menu.style.display === "block") {
                        menu.style.display = "none";
                    }
                });
            }
        });
    });
</script>
