<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Tabla de multiplicar</h1>
    <form action="Tabla.php" method="post">
        <label for="numero">Introduce un número</label>
        <input type="number" name="numero" id="numero">
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
<?php
if(isset($_POST['numero'])){
    $numero = $_POST['numero'];
    for($i = 1; $i <= 10; $i++){
        $resultado = $numero * $i;
        echo $numero . " x " . $i . " = " . $resultado . "<br>";
    }
}