// static/js/lightbox.js

document.addEventListener('DOMContentLoaded', function () {
  const lightboxLinks = document.querySelectorAll('.lightbox-link');
  const lightbox = document.querySelector('.lightbox');

  lightboxLinks.forEach(link => {
    link.addEventListener('click', function (e) {
      e.preventDefault();
      const imageUrl = this.getAttribute('data-image-url');
      const imageElement = document.createElement('img');
      imageElement.src = imageUrl;
      lightbox.innerHTML = '';
      lightbox.appendChild(imageElement);
      lightbox.style.display = 'flex';
    });
  });

  lightbox.addEventListener('click', function () {
    lightbox.style.display = 'none';
  });
});
