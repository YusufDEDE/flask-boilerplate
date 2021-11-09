document.addEventListener('DOMContentLoaded', function () {
    document.getElementById("footer-desc").title = "Simple JS DOM Manipulation!"
}, false);

document.onreadystatechange = function () {
  document.getElementById("footer-desc").innerHTML = "Simple JS DOM Manipulation!"
}