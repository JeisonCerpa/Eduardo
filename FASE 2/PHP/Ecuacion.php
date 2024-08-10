<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<style>
    .triangle {
    align-items: center;
     width: 0px;
    height: 0px;
    border-left: 50px solid transparent;
    border-right: 50px solid transparent;
    border-bottom: 100px solid #999;
    margin: 0 auto;
    }
    
    body{
        text-align: center;
        background-color: #f2f2f2;
        font-family: Arial, sans-serif;
        padding: 20px;
    }
    h1{
        color: blue;
        font-size: 30px;
        text-decoration: underline;
    }
    input{
        border: 2px solid blue;
        border-radius: 5px;
        padding: 5px;
        ont-size: 16px;
        margin: 10px;
    }
    label{
        color: black ;
        font-size: 20px;
        font-weight: bold;
        margin: 10px;
    }
    
</style>
<body>
    <h1>Ecuación</h1>
    <form action="Ecuacion.php" method="post">
        <label for="a">Valor de a:</label>
        <input type="text" name="a" id="a">
        <br>
        <label for="b">Valor de b:</label>
        <input type="text" name="b" id="b">
        <br>
        <input type="submit" value="Calcular">
    </form>
    <div class="triangle"></div>
</body>
</html>
<?php
    if(isset($_POST['a']) && isset($_POST['b'])){
        $a = $_POST['a'];
        $b = $_POST['b'];
        if($a == 0){
            echo "No se puede dividir por 0";
        }else{
            $x = -$b/$a;
            echo "El valor de x es: $x";
        }
    }