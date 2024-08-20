<?php
session_start();

// Inicializar la lista de tripulantes si no existe
if (!isset($_SESSION['tripulantes'])) {
    $_SESSION['tripulantes'] = [];
}

// Capturar el nombre y peso del tripulante
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = trim($_POST['nombre']);
    $peso = floatval($_POST['peso']);

    if ($nombre != "" && $peso > 0) {
        $_SESSION['tripulantes'][] = ['nombre' => $nombre, 'peso' => $peso];
    }
}

// Verificar si hay suficientes tripulantes para formar parejas
if (count($_SESSION['tripulantes']) >= 6) {
    $tripulantes = $_SESSION['tripulantes'];
    $parejas_encontradas = [];
    $pareja_minima = null;

    // Formar las parejas y verificar el peso
    for ($i = 0; $i < count($tripulantes); $i++) {
        for ($j = $i + 1; $j < count($tripulantes); $j++) {
            $peso_total = $tripulantes[$i]['peso'] + $tripulantes[$j]['peso'];
            if ($peso_total <= 150) {
                $parejas_encontradas[] = [
                    'tripulante1' => $tripulantes[$i]['nombre'],
                    'tripulante2' => $tripulantes[$j]['nombre'],
                    'peso_total' => $peso_total
                ];

                if ($pareja_minima === null || $peso_total < $pareja_minima['peso_total']) {
                    $pareja_minima = [
                        'tripulante1' => $tripulantes[$i]['nombre'],
                        'tripulante2' => $tripulantes[$j]['nombre'],
                        'peso_total' => $peso_total
                    ];
                }
            }
        }
    }

    // Mostrar las parejas encontradas y la pareja con el menor peso
    echo "<h1>Parejas Encontradas</h1>";
    if (empty($parejas_encontradas)) {
        echo "<p>No se encontraron parejas que cumplan con el peso máximo de 150 kg.</p>";
    } else {
        echo "<ul>";
        foreach ($parejas_encontradas as $pareja) {
            echo "<li>{$pareja['tripulante1']} y {$pareja['tripulante2']} - Peso Total: {$pareja['peso_total']} kg</li>";
        }
        echo "</ul>";

        echo "<h2>Pareja con el menor peso</h2>";
        echo "<p>{$pareja_minima['tripulante1']} y {$pareja_minima['tripulante2']} - Peso Total: {$pareja_minima['peso_total']} kg</p>";
    }

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
    <title>Formar Parejas de Tripulantes</title>
</head>
<body>
    <h1>Nave Espacial - Formar Parejas de Tripulantes</h1>

    <form action="" method="POST">
        <label for="nombre">Nombre del Tripulante:</label><br>
        <input type="text" id="nombre" name="nombre" required><br><br>

        <label for="peso">Peso del Tripulante (kg):</label><br>
        <input type="number" id="peso" name="peso" step="0.1" required><br><br>

        <button type="submit">Agregar Tripulante</button>
    </form>

    <h2>Tripulantes Ingresados:</h2>
    <ul>
        <?php
        if (!empty($_SESSION['tripulantes'])) {
            foreach ($_SESSION['tripulantes'] as $tripulante) {
                echo "<li>{$tripulante['nombre']} - {$tripulante['peso']} kg</li>";
            }
        }
        ?>
    </ul>

    <?php if (count($_SESSION['tripulantes']) >= 6): ?>
        <form action="" method="POST">
            <button type="submit">Generar Parejas</button>
        </form>
    <?php endif; ?>
</body>
</html>
