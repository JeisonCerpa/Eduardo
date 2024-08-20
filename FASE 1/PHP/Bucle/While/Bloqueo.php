<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Verificación de PIN</title>
</head>
<style>
    body    {
        font-family: Arial, sans-serif;
        align-items: center;
        display: flex;
        justify-content: center;
        height: 50vh;
        margin: 0;
        align-text: center;
    }
    input {
        margin: 10px;
    }
    form {
        margin: 10px;
    }
    p {
        margin: 10px;
    }

</style>
<body>
    <form method="post" action="">
        <p>Ingrese su PIN de 4 números:</p>
        <input type="text" name="pin" pattern="\d{4}" required>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
<?php
session_start();
$pin_correcto = "1234";
if (!isset($_SESSION['intentos'])) {
    $_SESSION['intentos'] = 0;
}
if ($_POST) {
    $pin_ingresado = $_POST['pin'];
    if ($pin_ingresado == $pin_correcto) {
        echo "PIN correcto.";
        session_destroy(); 
        exit;
    } else {
        $_SESSION['intentos']++;
        if ($_SESSION['intentos'] >= 3) {
            echo "Llamando a la policía.";
            session_destroy(); 
            exit;
        } else {
            echo "PIN incorrecto. Te quedan " . (3 - $_SESSION['intentos']) . " intentos.<br>";
        }
    }
}
?>

