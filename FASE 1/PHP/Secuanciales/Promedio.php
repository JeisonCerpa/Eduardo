<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Promedio.php" method="post">
        <label>Ingrese su primera nota: </label>
        <input type="number" name="nota1" id="nota1" step='0.1'><br>
        <label>Ingrese su segunda nota: </label>
        <input type="number" name="nota2" id="nota2" step='0.1'><br>
        <label>Ingrese su tercera nota: </label>
        <input type="number" name="nota3" id="nota3" step='0.1'><br>
        <button type='submit'>Calcular</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $nota1=$_POST['nota1']; $nota2=$_POST['nota2'];  $nota3=$_POST['nota3'];
    $promedio=($nota1+$nota2+$nota3)/3;
    echo "El promedio es: ".$promedio;
}
