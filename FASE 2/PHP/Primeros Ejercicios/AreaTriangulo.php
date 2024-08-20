<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    form {
        margin: 0 auto;
        width: 300px;
        padding: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: black;
    }
    h1 {
        text-align: center;
    }

    body {
        background-color: #f0f0f0;
        font-family: Arial, sans-serif;
        text-align: center;
    }

    label {
        display: inline-block;
        width: 255px;
        text-align: center;
    }

    input[type="number"] {
        width: 100px;
        height: 20px;
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 5px;
        margin: 5px;
        display: inline-block;
    }

    input[type="submit"] {
        width: 100px;
        height: 30px;
        border-radius: 5px;
        border: 1px solid #ccc;
        padding: 5px;
        margin: 5px;
        background-color: #4CAF50;
        color: white;
    }
</style>
<body>
    <h1>Calculadora de Area de un Triangulo</h1>
    <form action="AreaTriangulo.php" method="post">
        <label for="cateto">Ingresa el valor del primer cateto: </label>
        <input type="number" name="cateto1" id="cateto1"><br>
        <label for="cateto">Ingresa el valor del segundo cateto: </label>
        <input type="number" name="cateto2" id="cateto2"><br>
        <label for="grado">Ingresa el valor del angulo θ: </label>
        <input type="number" name="grado" id="grado"><br>
        <input type="submit" value="Calcular">
    </form>
</body>
</html>
<?php
if($_POST){
    $cateto1 = $_POST['cateto1'];
    $cateto2 = $_POST['cateto2'];
    $grado = $_POST['grado'];
    if($cateto1 <= 0 || $cateto2 <= 0 || $grado <= 0){
        echo "Los valores ingresados deben ser mayores a 0";
        return;
    }
    else{ 
        $radianes = deg2rad($grado);
        $area = ($cateto1 * $cateto2 * sin($radianes)) / 2;
        echo "El area del triangulo es: $area";
    }
}