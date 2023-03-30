

var button = document.createElement("button"); // to create the button
button.innerHTML = "Click me ! "; // for the text on the button

// 2. Append somewhere -> voegen aan html body
var body = document.getElementsByTagName("body")[0];
body.appendChild(button);


// style:
class buttonStyle {
    constructor(element) {
        element.style.width = "100px"
        element.style.height = "100px";
        element.style.backgroundColor = "blue";
        element.style.color = "white";
        element.style.fontFamily  = 'topSecretStamp';
    }
  }
const style_maken = new buttonStyle (button);


// 3. hover
button.addEventListener("mouseover", mouseOver);
button.addEventListener("mouseout", mouseOut);

function mouseOver() {
    button.style.background = "red";
    button.style.textDecoration = "underline";
}

function mouseOut() {
    button.style.background = "blue";
    button.style.textDecoration = "none";
}

// 3. event handler

button.addEventListener ("click", function(){
    var element = document.getElementById("demo");
    if (element.innerHTML === "Welkom") {
      element.innerHTML = "Welkom Israa!";
    } else {
      element.innerHTML = "Welkom";
    }
  });