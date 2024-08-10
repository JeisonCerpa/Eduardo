<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action ="PlayXbox.php" method="post">
        <label>Ingrese la cantidad de PlayStation 5 vendidos: </label>
        <input type="number" id="play" name="play" required><br>

        <label>Ingrese la cantidad de Xbox vendidos: </label>
        <input type="number" id="xbox" name="xbox" required><br>
        <button type="submit">Enviar</button>
    </form>
</body>
</html>

<?php
if($_POST){
    $pesoplay=(float)2.3; $pesoxbox=(float)3.2; $costoenvio=5;
    $play=$_POST['play']; $xbox=$_POST['xbox'];
    $pesopaquete=(($play*$pesoplay)+($pesoxbox*$xbox));
    $costototal=($pesopaquete*$costoenvio);
    echo 'El peso total de el paquete son: ' . $pesopaquete . ' libras.<br>';
    echo 'El costo total de el envio son : $' . $costototal;
 }
?>