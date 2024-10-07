<?php
$servidor = "localhost";
$database = "empleados";
$username = "root";
$password = "";
$conectar = mysqli_connect($servidor, $username, $password, $database);

if ($conectar->connect_error) {
    die("Error de conexión: " . $conectar->connect_error);
}
if ($_POST) {
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $puesto = $_POST['puesto'];
    $salario = $_POST['salario'];

    // Preparar la consulta
    $sql = "INSERT INTO empleados (nombre, apellido, puesto, salario) VALUES (?, ?, ?, ?)";

    $stmt = $conectar->prepare($sql);
    $stmt->bind_param("sssi", $nombre, $apellido, $puesto, $salario);

    if ($stmt->execute()) {
        $mensaje = "Registro ingresado";
    } else {
        $mensaje = "Error: " . $stmt->error;
    }
    $stmt->close();
    $conectar->close();
} else {
    $mensaje = "Por favor, complete el formulario.";
}
