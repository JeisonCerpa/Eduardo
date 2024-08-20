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
    <h1>Seleccione la altura de el arbol</h1>
    <form method="post" action="Arbol%20de%20Navidad.php">
        <input type="number" name="altura" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    $nivel = 1;
    if ($_POST){
        $altura = $_POST['altura'];
        echo '<br>';
        while ($nivel <= $altura) {
            $espacios = str_repeat('', ($altura - $nivel));
            $asteriscos = str_repeat('*', (2 * $nivel - 1));
            echo $espacios . $asteriscos . '<br>';
            $nivel++;
        }
        echo str_repeat(' ' , ($altura - 2)) , '|' , '|', '|';
    }
    
    ?>
</body>
</html>