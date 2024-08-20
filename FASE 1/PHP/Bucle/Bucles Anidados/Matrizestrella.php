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
    <form action="Matrizestrella.php" method="post">
        <input type="text" name="tamaño">
        <input type="submit" value="Enviar">
    </form>
    <?php
        if($_POST){
            $tamaño = $_POST['tamaño'];
            echo  "<br>";
            for ($i=0; $i < $tamaño; $i++) { 
                for ($j=0; $j < $tamaño; $j++) {
                    if($i == intdiv($tamaño, 2) or $j == intdiv($tamaño, 2)){
                        echo "1 ";
                    }elseif($i==0 or $i==$tamaño-1 or $j==0 or $j==$tamaño-1){
                        echo "0 ";
                    }else{
                        echo "1 ";
                    }
                }
                echo "<br>";
            }
        }
    ?>
</body>
</html>