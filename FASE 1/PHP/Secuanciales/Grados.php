<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Grados.php" method="post">
        <label>Ingrese los grados Fahrenheit: </label>
        <input type="number" name="grados" id="grados" step='0.1'><br>
        <button type='submit'>Convertir</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $grados=$_POST['grados'];
    $centigrados=(($grados-32)*(5/9));
    echo "El resultado son: ".$centigrados;
}
