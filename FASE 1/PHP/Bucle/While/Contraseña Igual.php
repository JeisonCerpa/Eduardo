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
    <h1>Confirmación de contraseña</h1>
    <form method="post" action="Contraseña Igual.php">
        <input type="password" name="contraseña" required>
        <input type="password" name="confirmar" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if ($_POST){
        $contraseña = $_POST['contraseña'];
        $confirmar = $_POST['confirmar'];
        if ($contraseña === $confirmar) {
            echo "Contraseña confirmada.";
        } else {
            echo "Las contraseñas no coinciden. Intente de nuevo.";
        }
    }
    ?>
</body>
</html>