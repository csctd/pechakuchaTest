document.addEventListener("DOMContentLoaded", function() {
    let slideshows = document.querySelectorAll('.pechakucha-slideshow');

    slideshows.forEach(function(slideshow) {
        let slides = slideshow.getElementsByTagName('figure');
        let currentIndex = 0;

        // Get the transition_time value from the pechakucha directive
        let transitionTime = parseInt(slideshow.getAttribute('data-transition-time')) || 1000; // Default to 1000 ms (1 second)

        let slideInterval = setInterval(nextSlide, transitionTime);

        function nextSlide() {
            slides[currentIndex].style.display = 'none';
            currentIndex = (currentIndex + 1) % slides.length;
            slides[currentIndex].style.display = 'block';
        }

        // Initialize the slideshow
        Array.from(slides).forEach((slide, index) => {
            slide.style.display = index === 0 ? 'block' : 'none';
        });
    });
});
