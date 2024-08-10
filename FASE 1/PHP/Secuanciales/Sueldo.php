<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action ="Sueldo.php" method="post">
        <fieldset>
        <label>Ingrese el valor de las horas: </label>
        <input type="text" id="valorhora" name="valorhora" required>
        </fieldset>
        <fieldset>
        <label>Ingrese las horas trabajadas: </label>
        <input type="text" id="horastrabajadas" name="horastrabajadas" required>
        </fieldset>
        <button type="submit">Enviar</button>

    </form>
</body>
</html>

<?php
if($_POST){
    $valorhora=$_POST["valorhora"]; $horastrabajadas=$_POST["horastrabajadas"];
    print "El sueldo total es: " . $valorhora*$horastrabajadas;
}

?>