<?php
function esPrimo($numero) {
    if ($numero <= 1) {
        return false;
    }

    for ($i = 2; $i <= sqrt($numero); $i++) {
        if ($numero % $i == 0) {
            return false;
        }
    }

    return true;
}

// Procesar el formulario cuando se envíe
$resultado = "";
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $numero = intval($_POST['numero']);

    if (esPrimo($numero)) {
        $resultado = "El número $numero es primo.";
    } else {
        $resultado = "El número $numero no es primo.";
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Verificar si un número es primo</title>
</head>
<body>
    <h1>Verificar si un número es primo</h1>

    <form action="" method="POST">
        <label for="numero">Ingresa un número:</label><br>
        <input type="number" id="numero" name="numero" required><br><br>
        <button type="submit">Verificar</button>
    </form>

    <?php
    if ($resultado != "") {
        echo "<h2>Resultado:</h2>";
        echo "<p>$resultado</p>";
    }
    ?>
</body>
</html>
