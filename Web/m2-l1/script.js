let zag1 = document.querySelector("h1");
let zag2 = document.querySelector("h2");
let one = document.querySelector('#one');
let checkone = document.querySelector('p:nth-child(1)');
let evenP = document.querySelectorAll(".even");
let checkevenP = document.querySelectorAll("p:nth-child(even)");
let colored = document.querySelectorAll(".colored");
let checkcoloredcount = 0;
let checkevenPcount = 0;
let checkcolored = [document.querySelector("p:nth-child(2)"), document.querySelector("p:nth-child(4)"), document.querySelector("p:nth-child(5)")];
let two = document.querySelector('.two');
let checktwo = document.querySelector("p:nth-child(2)");
let win;
if (one==checkone && window.getComputedStyle(one).color=="rgb(104, 58, 210)") {
    zag1.innerHTML = "Tarea 2";
    zag2.innerHTML = "Asigne a cada párrafo par la clase par. <br> Establece el tamaño de fuente en 18 píxeles y la negrita en 600.";
}
for (i=0; i<evenP.length; i++) {
    if (evenP[i]==checkevenP[i] && window.getComputedStyle(evenP[i]).fontSize == "18px" && window.getComputedStyle(evenP[i]).fontWeight == "600") {
        checkevenPcount +=1;
    }
}
if (checkevenPcount == evenP.length && evenP.length!=0) {
    zag1.innerHTML = "Tarea 3";
    zag2.innerHTML = "Asigne los párrafos segundo, cuarto y quinto a la clase coloreada. <br> Establecer su color de texto en rojo";
}
for (i=0; i< colored.length; i++) {
    if (colored[i] ==checkcolored[i] && window.getComputedStyle(checkcolored[i]).color == "rgb(255, 0, 0)") {
        checkcoloredcount +=1;
    }
}
if (checkcoloredcount==colored.length && checkcoloredcount!=0) {
    zag1.innerHTML = "Tarea 4";
    zag2.innerHTML = "Dale al segundo párrafo un ID de dos. <br> Establezca su color de texto en verde. <br> Nota: el selector de ID está encima del selector de clase";
}
if (two==checktwo && window.getComputedStyle(two).fontWeight == "600") {
    document.body.innerHTML = "";
    document.body.innerHTML+="<div class='win'> <div class='splash'> <h1>¡Ganaste!</h1> <h2>Tome la parte del código: 29Bp5rcd</h2>  </div> </div>"
    win = document.querySelector(".win");
    win.style.display = "flex";
    win.classList.add("anim");
}