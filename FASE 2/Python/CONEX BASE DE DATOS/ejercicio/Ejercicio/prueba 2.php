<?php
$servidor = "localhost";
$database = "empleados";
$username = "root";
$password = "";
$conectar = mysqli_connect($servidor, $username, $password, $database);

if ($conectar->connect_error) {
    die("Error de conexión: " . $conectar->connect_error);
}

if (isset($_POST['accion'])) {
    $accion = $_POST['accion'];

    switch ($accion) {
        case 'consultar':
            $cedula = $_POST['cedula'];

            if (!empty($cedula)) {
                $sql = "SELECT * FROM usuarios WHERE id = cedula";
                $stmt = $conectar->prepare($sql);
                $result = mysqli_query($conectar, $sql);
                if (mysqli_num_rows($result) > 0) {

                    $row = mysqli_fetch_assoc($result);

                    echo "<script>
                        document.getElementById('eliminar').style.display = 'inline';
                        document.getElementById('actualizar').style.display = 'inline';
                    </script>";
                } else {
                    echo "No se encontraron resultados.";
                }
            } else {
                echo "Por favor, ingrese un ID válido.";
            }
            break;

        case 'insertar':
            // Lógica para insertar un nuevo registro
            break;

        case 'eliminar':
            // Lógica para eliminar un registro
            break;

        case 'actualizar':
            // Lógica para actualizar un registro
            break;

        case 'salir':
            // Lógica para salir
            break;
    }
}

