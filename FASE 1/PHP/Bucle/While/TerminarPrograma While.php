<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>¿Desea terminar el programa?</h1>
    <form method="post" action="a.php">
        <input type="text" name="respuesta" required>
        <input type="submit" value="Enviar">
    </form>
    <?php
    if ($_POST){
        $respuesta = $_POST['respuesta'];
        while (TRUE) {
                if ($respuesta === 's') {
                    echo "Programa terminado.";
                    break;
                } else {
                    echo "Respuesta no válida. Intente de nuevo.<br>";
                    header("Refresh:0");
                    break;
                }
            #break;
        }
    }
    ?>

</body>
</html>