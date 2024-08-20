<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Ingrese hasta que numero quiere que salga</h1>
    <form action="Fibonacci While.php" method="post">
        <input type="text" name="numero" place>
        <input type="submit" value="Enviar">
    </form>
    <?php
        if(isset($_POST['numero'])){
            $numero = $_POST['numero'];
            $fib = 0;
            $fib2 = 1;
            $fib3 = 0;
            echo $fib . "<br>";
            echo $fib2 . "<br>";
            while($numero > $fib){
                echo $fib . "<br>";
                $fib3 = $fib + $fib2;
                $fib = $fib2;
                $fib2 = $fib3;
            }
        }
    ?>
</body>
</html>