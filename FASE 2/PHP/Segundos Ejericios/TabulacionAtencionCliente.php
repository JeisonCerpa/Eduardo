<?php
session_start();

// Inicializar la lista de calificaciones si no existe
if (!isset($_SESSION['calificaciones'])) {
    $_SESSION['calificaciones'] = [];
}

// Capturar la calificación
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $calificacion = intval($_POST['calificacion']);

    if ($calificacion >= 1 && $calificacion <= 5) {
        $_SESSION['calificaciones'][] = $calificacion;
    }
}

// Verificar si hay suficientes calificaciones para calcular el promedio
$promedio = 0;
$total_calificaciones = count($_SESSION['calificaciones']);

if ($total_calificaciones >= 10) {
    $suma = array_sum($_SESSION['calificaciones']);
    $promedio = $suma / $total_calificaciones;

    // Mostrar el promedio y limpiar la sesión
    echo "<h1>Promedio de Calificaciones</h1>";
    echo "<p>El promedio de calificaciones de $total_calificaciones personas es: " . number_format($promedio, 2) . "</p>";
    session_destroy();
    exit();
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calificación de Atención al Cliente</title>
</head>
<body>
    <h1>Califique el Servicio de Atención al Cliente</h1>

    <form action="" method="POST">
        <label for="calificacion">Elija una calificación del 1 al 5:</label><br><br>

        <?php
        // Array de opciones de calificación
        $opciones = [1, 2, 3, 4, 5];
        foreach ($opciones as $opcion) {
            echo "<input type='radio' id='calificacion$opcion' name='calificacion' value='$opcion' required>";
            echo "<label for='calificacion$opcion'>$opcion</label><br>";
        }
        ?>

        <br>
        <button type="submit">Enviar Calificación</button>
    </form>

    <h2>Calificaciones Recibidas: <?php echo $total_calificaciones; ?></h2>
</body>
</html>
