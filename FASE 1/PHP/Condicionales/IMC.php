<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action ="IMC.php" method="post">
        <label>Su altura: </label>
        <input type="text" id="altura" name="altura" required><br>

        <label>Ingrese su peso: </label>
        <input type="text" id="peso" name="peso" required><br>
        <button type="submit">Enviar</button>

    </form>
</body>
</html>

<?php
if($_POST){
    $altura=$_POST["altura"]; $peso=$_POST["peso"];
    $imc=(($peso)/($altura)**2);
    if($imc<18.5){
        echo "Esta bajo de peso";
    }
    elseif($imc>=18.5 && $imc<=24.9){
        echo "Su peso es adecuado, su imc es de: ".$imc;
    }
    elseif($imc>=25.0 && $imc<30){
        echo "Esta en sobrepeso, su imc es de: ".$imc;
    }
    elseif($imc>=30.0 && $imc<35){
        echo "Tiene un Obesidad grado 1, su imc es de: ".$imc;
    }
    elseif($imc>=35.0 && $imc<40){
        echo "Tiene un Obesidad grado 2, su imc es de: ".$imc;
    }
    else{
        echo "Tiene un Obesidad grado 3, su imc es de: ".$imc;
    }
}


?>