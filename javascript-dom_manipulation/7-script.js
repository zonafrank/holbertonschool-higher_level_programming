const url = "https://swapi-api.hbtn.io/api/films/?format=json";

function handleData(data) {
  const listMovies = document.querySelector("#list_movies");
  for (let movie of data.results) {
    const listItem = document.createElement("li");
    listItem.textContent = movie.title;
    listMovies.appendChild(listItem);
  }
}

fetch(url)
  .then((response) => response.json())
  .then(handleData)
  .catch(console.err);
