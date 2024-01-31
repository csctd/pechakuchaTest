document.addEventListener('DOMContentLoaded', function() {
    let slideIndex = 0;
    let slides = document.getElementsByClassName('pechakucha-slide');
    let transitionTime = document.querySelector('.pechakucha-slideshow').dataset.transitionTime;
    let progressContainer = document.querySelector('.pechakucha-progress');

    // Create and append progress indicators
    for (let i = 0; i < slides.length; i++) {
        let dot = document.createElement('span');
        dot.classList.add('pechakucha-progress-dot');
        dot.addEventListener('click', (function(index) {
            return function() {
                moveSlide(index - slideIndex);
            };
        })(i));
        progressContainer.appendChild(dot);
    }

    function showSlides() {
        updateSlidesAndDots();
        slideIndex++;
        if (slideIndex >= slides.length) { slideIndex = 0; }
        setTimeout(showSlides, transitionTime);
    }

    function moveSlide(direction) {
        slideIndex += direction;
        if (slideIndex >= slides.length) { slideIndex = 0; }
        if (slideIndex < 0) { slideIndex = slides.length - 1; }
        updateSlidesAndDots();
    }

    function updateSlidesAndDots() {
        for (let i = 0; i < slides.length; i++) {
            slides[i].style.display = 'none';
            progressContainer.children[i].classList.remove('active');
        }
        slides[slideIndex].style.display = 'block';
        progressContainer.children[slideIndex].classList.add('active');
    }

    document.getElementById('prev-slide').addEventListener('click', function() {
        moveSlide(-1);
    });
    document.getElementById('next-slide').addEventListener('click', function() {
        moveSlide(1);
    });

    // Initialize the slideshow
    showSlides();
});
