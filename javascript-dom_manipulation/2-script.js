const header = document.querySelector('header');
const idRedHeader = document.querySelector('#red_header');

idRedHeader.addEventListener('click', () => {
  header.classList.add('red');
});
