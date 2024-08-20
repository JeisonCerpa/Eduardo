<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="Bloqueo.php" method="post">
        <h1>Ingrese un PIN</h1>
         <input type="number" name="pin" id="pin">
         </form>

<?php
    for ($i=3; $i >= 0; $i--){
        echo '<form action="Bloqueo.php" method="post">';
        echo '<h1>Ingrese un PIN</h1>';
        echo '<input type="number" name="pin" id="pin" required>';
        echo '</form>';
        if($_POST){
            $pin = $_POST['pin'];
             if($pin == 1234){
                echo "PIN correcto";
                break;
            }
            else{
                echo 'PIN Incorrecto, intentos'. $i ;
                if ($i == 0){
                echo'Maximos intentos<br>';
                echo'Llamando a la policia';
             } 
        }
    }
}
?>
    </body>
</html>