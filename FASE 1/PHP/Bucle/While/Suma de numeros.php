<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Ingresa un numero(numero 0 para detener)</h1>
    <form method="post" action="Suma de numeros.php">
        <input type="number" name="numero" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if ($_POST){
        session_start();
        $numero = $_POST['numero'];
        if(!isset($_SESSION['suma'])){
            $_SESSION['suma'] = 0;
        }
        if ($numero == 0) {
            echo "La suma de los numeros es: " . $_SESSION['suma'] . '<br>';
            session_destroy();
        } else {
            $_SESSION['suma'] += $numero;
        }
    }
    ?>
</body>
</html>