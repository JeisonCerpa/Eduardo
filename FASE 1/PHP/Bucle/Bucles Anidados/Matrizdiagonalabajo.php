<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    body{
        text-align: center;
    }
</style>
<body>
    <h1>Digite el tamaño de la Matriz</h1>
    <form action="Matrizdiagonalabajo.php" method="post">
        <input type="text" name="tamaño">
        <input type="submit" value="Enviar">
    </form>
    <?php
        if($_POST){
            $tamaño = $_POST['tamaño'];
            echo  "<br>";
            for ($i=0; $i < $tamaño; $i++) { 
                for ($j=0; $j < $tamaño; $j++) { 
                    if($i >= $tamaño - 1 - $j){
                        echo "1 ";
                    }else{
                        echo "0 ";
                    }
                }
                echo "<br>";
            }
        }
    ?>
</body>
</html>