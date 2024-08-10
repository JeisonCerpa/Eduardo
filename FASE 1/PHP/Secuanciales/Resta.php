<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Resta.php" method="post">
        <label>Ingrese un numero: </label>
        <input type="number" name="resta" id="resta" step='0.1'><br>
        <button type='submit'>Restar 15%</button>
    </form>
</body>
</html>
<?php
if($_POST){
    $resta=$_POST['resta'];
    $resta=$resta*0.85;
    echo "El resultado es: ".$resta;
}
