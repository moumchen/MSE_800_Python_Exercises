document.getElementById('alertBtn').addEventListener('click', function() {
    alert('Hello from JavaScript!');
});

document.getElementById("goToNewPage").addEventListener("click", function() {
    window.location.href = "/new";
});

document.getElementById("parameterInURL").addEventListener("click", function() {
    name = document.getElementById("nameText").value;
    age = document.getElementById("ageText").value;
    window.location.href = "/" + name + "/" + age;
});