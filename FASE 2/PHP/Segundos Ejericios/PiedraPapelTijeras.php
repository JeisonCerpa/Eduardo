<?php
// Inicializar el resultado en vacío
$resultado = "";

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $opciones = ['piedra', 'papel', 'tijeras'];
    $jugador = $_POST['opcion'];
    $computadora = $opciones[array_rand($opciones)];

    // Determinar el resultado
    if ($jugador == $computadora) {
        $resultado = "Empate, ambos eligieron $jugador.";
    } elseif (
        ($jugador == 'piedra' && $computadora == 'tijeras') ||
        ($jugador == 'papel' && $computadora == 'piedra') ||
        ($jugador == 'tijeras' && $computadora == 'papel')
    ) {
        $resultado = "¡Ganaste! Tú elegiste $jugador y la computadora eligió $computadora.";
    } else {
        $resultado = "Perdiste. Tú elegiste $jugador y la computadora eligió $computadora.";
    }
}
?>

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Piedra, Papel o Tijeras</title>
</head>
<body>
    <h1>Juega a Piedra, Papel o Tijeras</h1>

    <form action="" method="POST">
        <label for="opcion">Elige tu jugada:</label><br><br>
        <input type="radio" id="piedra" name="opcion" value="piedra" required>
        <label for="piedra">Piedra</label><br>
        <input type="radio" id="papel" name="opcion" value="papel" required>
        <label for="papel">Papel</label><br>
        <input type="radio" id="tijeras" name="opcion" value="tijeras" required>
        <label for="tijeras">Tijeras</label><br><br>

        <button type="submit">Jugar</button>
    </form>

    <?php
    if ($resultado != "") {
        echo "<h2>Resultado:</h2>";
        echo "<p>$resultado</p>";
    }
    ?>
</body>
</html>
