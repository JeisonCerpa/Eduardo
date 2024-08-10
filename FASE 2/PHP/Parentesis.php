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
    <h1>PARENTESIS</h1>
    <form action="Parentesis.php" method="post">
        <label for="parentesis">Ingresa el simbolo: </label>
        <input type="text" name="parentesis" id="parentesis">
        <input type="submit" value="Enviar"><br>
</body>
</html>
<?php
if ($_POST) {
    $parentesis = $_POST['parentesis'];
    if ($parentesis == "(") {
        echo "El simbolo ingresado es un parentesis abierto";
    } elseif ($parentesis == ")") {
        echo "El simbolo ingresado es un parentesis cerrado";
    } else {
        echo "El simbolo ingresado no es un parentesis";
    }
}