<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="LitrosKM.php" method="post">
        <label>Ingrese los kilometros recorridos: </label>
        <input type="number" name="km" id="km" step='0.1'><br>
        <label>Ingrese los litros consumidos: </label>
        <input type="number" name="litros" id="litros" step='0.1'><br>
        <button type='submit'>Enviar</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $km=$_POST['km']; $litros=$_POST['litros'];
    $consumo=$litros/$km;
    echo 'Su consumo por km es: '.$consumo;
}
