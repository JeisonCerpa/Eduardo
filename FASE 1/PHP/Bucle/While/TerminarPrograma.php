
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>Terminar Programa</title>
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
    <form method="post" action="TerminarPrograma.php">
        <p>¿Desea terminar el programa? (s/n)</p>
        <input type="text" name="respuesta" required>
        <input type="submit" value="Enviar">
    </form>
</body>
</html>
<?php
if ($_POST){
    $respuesta = '';
    echo '<br>';
        if ($_POST) {
            $respuesta = $_POST['respuesta'];
            if (strtolower($respuesta) === 's') {
                echo "Programa terminado.";
            } else {
                echo "Respuesta no válida. Intente de nuevo.<br>";
            }
        }
    }
?>
