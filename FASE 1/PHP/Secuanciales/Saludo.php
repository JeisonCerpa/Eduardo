<?php
if ($_POST){
// Obtener el nombre de los datos POST
$nombre = $_POST["nombre"];
}
    echo "<form action='#' method='post'>";
        echo "<label for='nombre'>Nombre:</label>";
        echo "<input type='text' id='nombre' name='nombre' required>";
        echo "<button type='submit'>Enviar</button>";
    echo "</form>";
    if (isset  ($nombre)) {
    echo "¡Hola, $nombre! ¿Cómo estás?";
    }    