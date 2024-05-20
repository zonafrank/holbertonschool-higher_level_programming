const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url)
  .then((response) => {
    return response.json();
  })
  .then((data) => {
    const character = document.querySelector('#character');
    character.textContent = data.name;
  })
  .catch((err) => {
    console.log(err);
  });
