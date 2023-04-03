var yearElem = document.getElementById("year");
var currentYear = new Date().getFullYear();
var yearRange = "2020-" + currentYear;
yearElem.innerHTML = "&copy; " + yearRange + " LePravda Group. Todos los derechos resevados.";

function showErrorPopup() {
    var popup = document.getElementById("error-popup");
    popup.style.display = "block";
    var closeButton = document.getElementById("close-button");
    closeButton.addEventListener("click", function() {
      popup.style.display = "none";
    });
  }

function closeErrorPopup() {
    var popup = document.getElementById("error-popup");
    popup.style.display = "none";
}

// fetch('/')
//   .then(response => response.json())
//   .then(data => {
//     const dynamicList = document.getElementById('dynamic-list');
//     data.forEach(item => {
//       const li = document.createElement('li');
//       li.innerText = `${item.name}: ${item.description}`;
//       dynamicList.appendChild(li);
//     });
//   });
