<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action ="IMC.php" method="post">
        <label>Su altura: </label>
        <input type="text" id="altura" name="altura" required><br>

        <label>Ingrese su peso: </label>
        <input type="text" id="peso" name="peso" required><br>
        <button type="submit">Enviar</button>

    </form>
</body>
</html>

<?php
if($_POST){
    $altura=$_POST["altura"]; $peso=$_POST["peso"];
    print "Su IMC es de:  " . (($peso)/($altura)**2);
}

?>