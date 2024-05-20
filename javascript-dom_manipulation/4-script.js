let addItem = document.querySelector("#add_item");
let list = document.querySelector(".my_list");

addItem.addEventListener("click", () => {
  let listItem = document.createElement("li");
  listItem.textContent = "Item";
  list.appendChild(listItem);
});
