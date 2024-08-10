
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calculator</title>
</head>
<body>
    <form action="Calculadora.php" method="post">
        <label>Primero numero: </label>
        <input type="number" name="num1" id="num1" step='0.1'><br>
        <label>Segundo numero: </label>
        <input type="number" name="num2" id="num2" step='0.1'><br>
        <label>Selecciona la operacion: </label>
        <select name="operation" id="operation">
            <option value="sum">+</option>
            <option value="sub">-</option>
            <option value="mul">*</option>
            <option value="div">/</option>
            <option value="exit">Exit</option>
        </select><br>
        <button type='submit'>Calculate</button>
    </form>
</body>
</html>
<?php
if($_POST) {
$num1 = $_POST['num1'];
$num2 = $_POST['num2'];
$operation = $_POST['operation'];

if ($operation == 'sum') {
    $result = $num1 + $num2;
    echo "Result: " . $result;
} elseif ($operation == 'sub') {
    $result = $num1 - $num2;
    echo "Result: " . $result;
} elseif ($operation == 'mul') {
    $result = $num1 * $num2;
    echo "Result: " . $result;
} elseif ($operation == 'div') {
    if ($num2 != 0) {
        $result = $num1 / $num2;
        echo "Result: " . $result;
    } else {
        echo "Error: Division by zero";
    }
} elseif ($operation == 'exit') {
    echo "Bye!";
    exit;
}
}
