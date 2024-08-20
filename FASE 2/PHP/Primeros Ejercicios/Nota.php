<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body {
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
        text-align: center;
    }

    h1 {
        color: #333333;
        text-align: center;
    }

    form {
        margin: 20px auto;
        width: 300px;
        background-color: #ffffff;
        padding: 20px;
        border-radius: 5px;
    }

    label {
        display: block;
        margin-bottom: 10px;
        color: #666666;
    }

    input[type="text"] {
        margin-bottom: 5px;
        width: 92%;
        padding: 10px;
        border: 1px solid #cccccc;
        border-radius: 3px;
    }

    input[type="submit"] {
        display: block;
        width: 100%;
        padding: 10px;
        background-color: #333333;
        color: #ffffff;
        border: none;
        border-radius: 3px;
        cursor: pointer;
    }

    input[type="submit"]:hover {
        background-color: #555555;
    }
</style>
<body>
    <h1>NOTAS</h1>
    <form action="Nota.php" method="post">
        <label for="nota">Ingresa la nota: </label>
        <input type="text" name="nota" id="nota">
        <input type="submit" value="Enviar"><br>
</body>
</html>
<?php
if ($_POST) {
    $nota = $_POST['nota'];
    if ($nota < 5) {
        echo "Suspenso";
    } elseif ($nota >= 5 && $nota < 7) {
        echo "Aprobado";
    } elseif ($nota >= 7 && $nota < 8.5) {
        echo "Notable";
    } elseif ($nota >= 8.5 && $nota < 10) {
        echo "Sobresaliente";
    } elseif ($nota == 10) {
        echo "Matrícula de honor";
    } 
    else {
        echo "Nota no válida";
    }
}