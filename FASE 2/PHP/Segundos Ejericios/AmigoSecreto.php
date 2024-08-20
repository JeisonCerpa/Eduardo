<?php
session_start();

// Inicializar las listas si no existen
if (!isset($_SESSION['hombres'])) {
    $_SESSION['hombres'] = [];
}
if (!isset($_SESSION['mujeres'])) {
    $_SESSION['mujeres'] = [];
}

// Lógica para capturar los nombres uno por uno
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST['nombre'];
    if ($nombre != "") {
        if (count($_SESSION['hombres']) < 5) {
            $_SESSION['hombres'][] = $nombre;
        } elseif (count($_SESSION['mujeres']) < 5) {
            $_SESSION['mujeres'][] = $nombre;
        }
    }
}

// Verificar si se han ingresado todos los nombres
if (count($_SESSION['hombres']) == 5 && count($_SESSION['mujeres']) == 5) {
    // Mezclar los arrays para hacer las parejas al azar
    shuffle($_SESSION['hombres']);
    shuffle($_SESSION['mujeres']);

    // Generar las parejas
    $parejas = array();
    for ($i = 0; $i < 5; $i++) {
        $parejas[] = $_SESSION['hombres'][$i] . " - " . $_SESSION['mujeres'][$i];
    }

    // Mostrar las parejas y limpiar la sesión
    echo "<h1>Parejas Generadas</h1>";
    echo "<ul>";
    foreach ($parejas as $pareja) {
        echo "<li>$pareja</li>";
    }
    echo "</ul>";

    // Limpiar la sesión para empezar de nuevo
    session_destroy();
    exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Amigo Secreto - Generador de Parejas</title>
</head>
<body>
    <h1>Generador de Parejas de Amigo Secreto</h1>

    <?php if (count($_SESSION['hombres']) < 5): ?>
        <h2>Ingresa el nombre de un hombre (<?= count($_SESSION['hombres']) + 1 ?> de 5):</h2>
    <?php elseif (count($_SESSION['mujeres']) < 5): ?>
        <h2>Ingresa el nombre de una mujer (<?= count($_SESSION['mujeres']) + 1 ?> de 5):</h2>
    <?php endif; ?>

    <form action="" method="POST">
        <input type="text" name="nombre" required>
        <button type="submit">Enviar</button>
    </form>

    <?php
    // Mostrar los nombres ya ingresados
    echo "<h3>Hombres:</h3><ul>";
    foreach ($_SESSION['hombres'] as $hombre) {
        echo "<li>$hombre</li>";
    }
    echo "</ul>";

    echo "<h3>Mujeres:</h3><ul>";
    foreach ($_SESSION['mujeres'] as $mujer) {
        echo "<li>$mujer</li>";
    }
    echo "</ul>";
    ?>
</body>
</html>
