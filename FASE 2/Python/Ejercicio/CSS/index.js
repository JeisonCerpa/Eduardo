const menuToggle = document.querySelector('.toggle');
const showcase = document.querySelector('.showcase');
const menuToggle2 = document.querySelector('.toggle2');

menuToggle2.addEventListener('click', () => {
  menuToggle2.classList.toggle('active');
  showcase.classList.toggle('active');
})


menuToggle.addEventListener('click', () => {
  menuToggle.classList.toggle('active');
  showcase.classList.toggle('active');
})
