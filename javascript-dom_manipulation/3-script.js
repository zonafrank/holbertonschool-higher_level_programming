const header = document.querySelector('header');
const idToggleHeader = document.querySelector('#toggle_header');

idToggleHeader.addEventListener('click', () => {
  header.classList.toggle('red');
  header.classList.toggle('green');
});
