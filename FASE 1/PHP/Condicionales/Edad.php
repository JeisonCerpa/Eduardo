<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Edad.php" method="post">
        <label>Que edad tienes? </label> 
        <input type="number" name="edad" id="edad" step='0.1'><br>
        <button type='submit'>Enviar</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $edad=$_POST['edad'];
    if($edad>=18){
        echo 'Eres mayor de edad';
    }else{
        echo 'Eres menor de edad';
    }
}