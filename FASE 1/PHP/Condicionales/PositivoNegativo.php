<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="PositivoNegativo.php" method="post">
        <label>Ingrese un numero: </label> 
        <input type="number" name="num" id="num" step='0.1'><br>
        <button type='submit'>Enviar</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $num=$_POST['num'];
    if($num>=0){
        echo 'El numero es positivo';
    }else{
        echo 'El numero es negativo';
    }
}