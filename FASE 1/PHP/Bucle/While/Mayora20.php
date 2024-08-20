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
</style>
<body>
    <h1>Numero mayor a 20</h1>
    <form method="post" action="Mayora20.php">
        <input type="number" name="numero" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if ($_POST){
        $num = $_POST['numero'];
        if ($num > 20) {
            echo "El numero es mayor a 20";
        } else {
            echo "El numero no es mayor a 20";
        }
    }
    ?>

</body>
</html>