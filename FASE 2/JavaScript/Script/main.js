var nombre = 'Jeison';
var edad = 25;
var concatenar = nombre + ' ' + edad;
document.write(concatenar);
var datos = document.getElementById("datos");
datos.innerHTML = `El nombre es: ${nombre} y la edad es: ${edad}`;

if(edad >= 18){
    datos.innerHTML += '<h1>Eres mayor de edad</h1>';}

for (let i = 2000; i <= 2024; i++) {
    datos.innerHTML += "<h2>Estamos en el año: " + i;
}
