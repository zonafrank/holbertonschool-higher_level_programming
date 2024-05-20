const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

function handleData (data) {
  const helloId = document.querySelector('#hello');
  helloId.textContent = data.hello;
}

fetch(url)
  .then((response) => response.json())
  .then(handleData)
  .catch(console.error);
