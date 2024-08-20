<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Fibonacci.php" method="post">
        <h1>Ingresa la cantidad de numeros en la suceccion Fibonacci</h1>
        <label for="numero">Ingresa el numero</label>
        <input type="number" name="numero" id="numero" required>
        <button type="submit">Calcular</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $num = $_POST['numero'];
    $f1 = 0;
    $f2 = 1;
    for($i = 1; $i <= $num; $i++){
        echo $f1. '<br>';
        $f3 = $f1+$f2;
        $f1  = $f2;
        $f2 = $f3;
    }
}