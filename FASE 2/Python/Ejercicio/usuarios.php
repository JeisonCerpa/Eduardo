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
            $cedula = $_POST['cedula'];
            // Verifica si se ingresó un ID válido
            if (!empty($cedula)) {
                // Evitar inyección SQL con mysqli_real_escape_string
                $cedula = mysqli_real_escape_string($conectar, $cedula);

                // Realiza la consulta
                $query = "SELECT * FROM usuarios WHERE cedula = '$cedula'";
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
                $cedula = $_POST['cedula'];
                $nombre = $_POST['nombre'];
                $apellido = $_POST['apellido'];
                $direccion = $_POST['direccion'];
                $telefono = $_POST['telefono'];
                $email = $_POST['email'];
                $password = $_POST['password'];
                // Preparar la consulta
                $sql = "INSERT INTO usuarios (cedula, nombre, apellido, direccion, telefono, email, password) VALUES (?, ?, ?, ?, ?, ?, ?)";

                $stmt = $conectar->prepare($sql);
                $stmt->bind_param("sssssss", $cedula, $nombre, $apellido, $direccion, $telefono, $email, $password);

                if ($stmt->execute()) {
                    $mensaje = "<script>alert('Registro ingresado.');</script>";
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
                $cedula = $_POST['cedula'];
                if (!empty($cedula)) {
                    $query = "DELETE FROM usuarios WHERE cedula = '$cedula'";
                    $result = mysqli_query($conectar, $query);
                    if ($result) {
                        echo "<script>alert('Registro eliminado correctamente.');</script>";
                    } else {
                        echo "<script>alert('Error al eliminar el registro.');</script>";   
                    }
                }
                break;

        case 'Actualizar':
            $cedula = $_POST['cedula'];
            $nombre = $_POST['nombre'];
            $apellido = $_POST['apellido'];
            $direccion = $_POST['direccion'];
            $telefono = $_POST['telefono'];
            $email = $_POST['email'];
            $password = $_POST['password'];

            $cedula = mysqli_real_escape_string($conectar, $cedula);
            $nombre = mysqli_real_escape_string($conectar, $nombre);
            $apellido = mysqli_real_escape_string($conectar, $apellido);
            $direccion = mysqli_real_escape_string($conectar, $direccion);
            $telefono = mysqli_real_escape_string($conectar, $telefono);
            $email = mysqli_real_escape_string($conectar, $email);  
            $password = mysqli_real_escape_string($conectar, $password);

            $query = "UPDATE usuarios SET nombre = '$nombre', apellido = '$apellido', direccion = '$direccion', telefono = '$telefono', email = '$email', password = '$password' WHERE cedula = '$cedula'";
            $result = mysqli_query($conectar, $query);
            if($result) {
                echo "<script>alert('Registro actualizado correctamente.');</script>";
            } else {
                echo "<scrpit>alert('Error al actualizar el registro.');</script>";
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
    <title>Usuarios</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>

<body>
    <h1>Datos de los Usuarios</h1>
    <section>
        <div class="title"><h2>Ingresa los datos</h2></div>
        <div class="usuarios">
            <form action="usuarios.php" method="POST">
                <label for="cedula">Cedula: </label>
                <input type="text" name="cedula" id="cedula" placeholder="Ingresa la cedula" required autofocus
                    value="<?php echo isset($row['cedula']) ? $row['cedula'] : ''; ?>"><br>
                <label for="nombre" class="label">Nombre: </label>
                <input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre"
                    value="<?php echo isset($row['nombre']) ? $row['nombre'] : ''; ?>"><br>
                <label for="apellido" class="label">Apellido: </label>
                <input type="text" name="apellido" id="apellido" placeholder="Ingresa el apellido"
                    value="<?php echo isset($row['apellido']) ? $row['apellido'] : ''; ?>"><br>
                <label for="direccion" class="label">Direccion: </label>
                <input type="text" name="direccion" id="direccion" placeholder="Ingresa la direccion"
                    value="<?php echo isset($row['direccion']) ? $row['direccion'] : ''; ?>"><br>
                <label for="telefono" class="label">Telefono: </label>
                <input type="text" name="telefono" id="telefono" placeholder="Ingresa el telefono"
                    value="<?php echo isset($row['telefono']) ? $row['telefono'] : ''; ?>"><br>
                <label for="email" class="label">Email: </label>
                <input type="text" name="email" id="email" placeholder="Ingresa el email"
                    value="<?php echo isset($row['email']) ? $row['telefono'] : ''; ?>"><br>
                <label for="password" class="label">Contraseña: </label>
                <input type="text" name="password" id="password" placeholder="Ingresa la contraseña"
                    value="<?php echo isset($row['password']) ? $row['password'] : ''; ?>"><br>
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
