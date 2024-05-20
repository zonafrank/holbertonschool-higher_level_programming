let header = document.querySelector("header");
let idToggleHeader = document.querySelector("#toggle_header");

idToggleHeader.addEventListener("click", () => {
  header.classList.toggle("red");
  header.classList.toggle("green");
});
