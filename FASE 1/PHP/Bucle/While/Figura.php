<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Figura</h1>
    <form method="post" action="Figura.php">
        <p>Ancho de la figura</p>
        <input type="number" name="lado1" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if($_POST){
        $lado1 = $_POST['lado1'];
        $nivel = 1;
        while ($nivel <= $lado1) {
            $asteriscos = str_repeat('*',(2*$nivel)-1);
            echo $asteriscos . '<br>';
            $nivel += 1;
    }
    while ($nivel > 1) {
        $nivel -= 1;
        $asteriscos = str_repeat('*',(2*$nivel)-1);
        echo $asteriscos . '<br>';
        $nivel -= 1;
    }
}
    ?>
</body>
</html>
