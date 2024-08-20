<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body {
        text-align: center;
    }
    form {
        margin-top: 20px;
    }
    input {
        margin-top: 10px;
    }
    h1 {
        margin-top: 150px;
    }
</style>
<body>
    <h1>Cuenta Regresiva</h1>
    <form method="post" action="CuentaRegresiva.php">
        <input type="number" name="numero" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if ($_POST){
        $numero = $_POST['numero'];
        echo '<br>';
        while ($numero >= 0) {
            echo $numero . '<br>';
            $numero--;
        }
    }
    ?>
</body>
</html>