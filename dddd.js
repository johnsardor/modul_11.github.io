// Carousel initialization
let carousel = document.querySelector('.carousel');
let carouselInner = carousel.querySelector('.carousel-inner');
let items = carouselInner.querySelectorAll('.item');
let activeIndex = 0;
let intervalTime = 3000; // Time between slide transitions (in milliseconds)

function changeSlide() {
  activeIndex = (activeIndex + 1) % items.length;
  carouselInner.style.transform = `translateX(-${activeIndex * 100}%)`;
}

setInterval(changeSlide, intervalTime);