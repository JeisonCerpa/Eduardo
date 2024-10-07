<?php
$servidor = "localhost";
$database = "ejercicio";
$username = "root";
$password = "";
$conectar = mysqli_connect($servidor, $username, $password, $database);

if ($conectar->connect_error) {
    die("Error de conexión: " . $conectar->connect_error);
}

$row = null;

$mostrarBotonesAccion = false;

if (isset($_POST['accion'])) {
    $accion = $_POST['accion'];

    switch ($accion) {
        case 'Consultar':
            // Recibe el ID del formulario
            $id_empleado = $_POST['id_empleado'];
            // Verifica si se ingresó un ID válido
            if (!empty($id_empleado)) {
                // Evitar inyección SQL con mysqli_real_escape_string
                $id_empleado = mysqli_real_escape_string($conectar, $id_empleado);

                // Realiza la consulta
                $query = "SELECT * FROM emplados WHERE id_empleado = '$id_empleado'";
                $result = mysqli_query($conectar, $query);

                // Verifica si hay resultados
                if ($result && mysqli_num_rows($result) > 0) {
                    // Carga los datos en un array asociativo
                    $row = mysqli_fetch_assoc($result);
                    $mostrarBotonesAccion = true;
                } else {

                    echo "<script>alert('No se encontraron resultados.');</script>";
                }
            } else {
                echo "<script>alert('Por favor, ingrese un ID válido.');</script>";
            }
            break;

        case 'Insertar':
            if ($_POST) {
                $nombre = $_POST['nombre'];
                $apellido = $_POST['apellido'];
                $correo_electronico = $_POST['correo_electronico'];
                $telefono = $_POST['telefono'];
                $cargo = $_POST['cargo'];
                $salario = $_POST['salario'];
                $fecha_contratacion = $_POST['fecha_contratacion'];
                // Preparar la consulta
                $sql = "INSERT INTO empleados (nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion) VALUES (?, ?, ?, ?, ?, ?, ?)";
                $stmt = $conectar->prepare($sql);
                $stmt->bind_param("sssssds", $nombre, $apellido, $correo_electronico, $telefono, $cargo, $salario, $fecha_contratacion);
                if ($stmt->execute()) {
                    $mensaje = "<script>alert('Registro insertado.');</script>";
                    echo $mensaje;
                } else {
                    $mensaje = "<script>alert('Error: " . $stmt->error . "');</script>";
                    echo $mensaje;
                }
                $stmt->close();
                $conectar->close();
            } else {
                $mensaje = "<script>alert('Por favor, complete el formulario.');</script>";
                echo $mensaje;
            }

            break;

            case 'Eliminar':
                $id_empleado = $_POST['id_empleado'];
                if (!empty($id_empleado)) {
                    $query = "DELETE FROM empleados WHERE id_empleado = '$id_empleado'";
                    $result = mysqli_query($conectar, $query);
                    if ($result) {
                        echo "<script>alert('Registro eliminado.');</script>";
                    } else {
                        echo "<script>alert('Error al eliminar el registro.');</script>";
                    }
                }
                break;

        case 'Actualizar':
            $id_empleado = $_POST['id_empleado'];
            $nombre = $_POST['nombre'];
            $apellido = $_POST['apellido'];
            $correo_electronico = $_POST['correo_electronico'];
            $telefono = $_POST['telefono'];
            $cargo = $_POST['cargo'];
            $salario = $_POST['salario'];
            $fecha_contratacion = $_POST['fecha_contratacion'];

            $id_empleado = mysqli_real_escape_string($conectar, $id_empleado);
            $nombre = mysqli_real_escape_string($conectar, $nombre);
            $apellido = mysqli_real_escape_string($conectar, $apellido);
            $correo_electronico = mysqli_real_escape_string($conectar, $correo_electronico);
            $telefono = mysqli_real_escape_string($conectar, $telefono);
            $cargo = mysqli_real_escape_string($conectar, $cargo);  
            $salario = mysqli_real_escape_string($conectar, $salario);
            $fecha_contratacion = mysqli_real_escape_string($conectar, $fecha_contratacion);

            $query = "UPDATE empleados SET nombre = '$nombre', apellido = '$apellido', correo_electronico = '$correo_electronico', telefono = '$telefono', cargo = '$cargo', salario = '$salario', fecha_contratacion = '$fecha_contratacion' WHERE id_empleado = '$id_empleado'";
            $result = mysqli_query($conectar, $query);
            if($result) {
                echo "<script>alert('Registro actualizado.');</script>";
            } else {
                echo "<script>alert('Error al actualizar el registro.');</script>";
            }
            break;

    }
}

?>
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Empleados</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>

<body>
    <h1>Datos de los Empleados</h1>
    <section>
        <div class="title"><h2>Ingresa los datos del empleado</h2></div>
        <div class="usuarios">
            <form action="empleados.php" method="POST">
                <label for="id_empleado">Id_Empleado: </label>
                <input type="text" name="id_empleado" id="id_empleado" placeholder="Ingresa el Id del Empleado" autofocus
                    value="<?php echo isset($row['id_empleado']) ? $row['id_empleado'] : ''; ?>"><br>
                <label for="nombre">Nombre: </label>
                <input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre"
                    value="<?php echo isset($row['nombre']) ? $row['nombre'] : ''; ?>"><br>
                <label for="apellido">Apellido: </label>
                <input type="text" name="apellido" id="apellido" placeholder="Ingresa el apellido"
                    value="<?php echo isset($row['apellido']) ? $row['apellido'] : ''; ?>"><br>
                <label for="correo_electronico">Correo Electronico: </label>
                <input type="text" name="correo_electronico" id="correo_electronico" placeholder="Ingresa El Correo  Electronico"
                    value="<?php echo isset($row['correo_electronico']) ? $row['correo_electronico'] : ''; ?>"><br>
                <label for="telefono">Telefono: </label>
                <input type="text" name="telefono" id="telefono" placeholder="Ingresa El # De Telefono"
                    value="<?php echo isset($row['telefono']) ? $row['telefono'] : ''; ?>"><br>
                <label for="cargo">Cargo: </label>
                <input type="text" name="cargo" id="cargo" placeholder="Ingresa El Cargo"
                    value="<?php echo isset($row['cargo']) ? $row['cargo'] : ''; ?>"><br>
                <label for="salario">Salario: </label>
                <input type="text" name="salario" id="salario" placeholder="Ingresa El Salario"
                    value="<?php echo isset($row['salario']) ? $row['salario'] : ''; ?>"><br>
                <label for="fecha_contratacion">Fecha de Contratacion: </label>
                <input type="date" name="fecha_contratacion" id="fecha_contratacion"
                    value="<?php echo isset($row['fecha_contratacion']) ? $row['fecha_contratacion'] : ''; ?>"><br>
                </div>
                <div class="botonescen">
                <div class="botones">
                    <input type="submit" value="Consultar" name="accion" class="btn btn-primary btn-large">
                    <input type="submit" value="Insertar" name="accion" class="btn btn-primary btn-large">
                    <?php if ($mostrarBotonesAccion): ?>
                    <button type="submit" name="accion" value="Actualizar" class="btn btn-primary btn-large">Actualizar</button>
                    <button type="submit" name="accion" value="Eliminar" class="btn btn-eliminar btn-large">Eliminar</button>
                    <?php endif; ?>
   
                    <button class="btn btn-primary btn-large"><a href="index.html">Salir</a></button>
                </div>
                </div>
            </form>
    </section>
</body>

</html>
<?php
