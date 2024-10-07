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
            $id_producto= $_POST['id_producto'];
            // Verifica si se ingresó un ID válido
            if (!empty($id_producto)) {
                // Evitar inyección SQL con mysqli_real_escape_string
                $id_producto = mysqli_real_escape_string($conectar, $id_producto);

                // Realiza la consulta
                $query = "SELECT * FROM productos WHERE id_producto = '$id_producto'";
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
                $id_producto = $_POST['id_producto'];
                $nombre = $_POST['nombre'];
                $descripcion = $_POST['descripcion'];
                $precio = $_POST['precio'];
                $fecha_venc = $_POST['fecha_venc'];
                
                // Preparar la consulta
                $sql = "INSERT INTO productos (id_producto, nombre, descripcion, precio, fecha_venc) VALUES (?, ?, ?, ?, ?)";
                $stmt = $conectar->prepare($sql);
                $stmt->bind_param("sssss", $id_producto, $nombre, $descripcion, $precio, $fecha_venc);

                if ($stmt->execute()) {
                    $mensaje = "<script>alert('Registro insertado correctamente.');</script>";
                    echo $mensaje;
                } else {
                    $mensaje = "<script>alert('Error: " . $stmt->error . "');</script>";
                    echo $mensaje;
                }
                $stmt->close();
                $conectar->close();
            } else {
                $mensaje = "<script>alert('Por favor, ingrese los datos.');</script>";
                echo $mensaje;
            }

            break;

            case 'Eliminar':
                $id_producto = $_POST['id_producto'];
                if (!empty($id_producto)) {
                    $query = "DELETE FROM productos WHERE id_producto = '$id_producto'";
                    $result = mysqli_query($conectar, $query);
                    if ($result) {
                        echo "<script>alert('Registro eliminado correctamente.');</script>";
                    } else {
                        echo "<script>alert('Error al eliminar el registro.');</script>";
                    }
                }
                break;

        case 'Actualizar':
            $id_producto = $_POST['id_producto'];
            $nombre = $_POST['nombre'];
            $descripcion = $_POST['descripcion'];
            $precio = $_POST['precio'];
            $fecha_venc = $_POST['fecha_venc'];
         

            $id_producto = mysqli_real_escape_string($conectar, $id_producto);
            $nombre = mysqli_real_escape_string($conectar, $nombre);
            $descripcion = mysqli_real_escape_string($conectar, $descripcion);
            $precio = mysqli_real_escape_string($conectar, $precio);
            $fecha_venc = mysqli_real_escape_string($conectar, $fecha_venc);
          

            $query = "UPDATE productos SET nombre = '$nombre', descripcion = '$descripcion', precio = '$precio', fecha_venc = '$fecha_venc' WHERE id_producto = '$id_producto'";
            $result = mysqli_query($conectar, $query);
            if($result) {
                echo "<script>alert('Registro actualizado correctamente.');</script>";
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
    <title>Productos</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>

<body>
    <h1>Datos de los Productos</h1>
    <section>
        <div class="title"><h2>Ingresa los datos</h2></div>
        <div class="usuarios">
            <form action="productos.php" method="POST">
                <label for="id_producto">ID del producto: </label>
                <input type="text" name="id_producto" id="id_producto" placeholder="Ingresa la id del producto" autofocus
                    value="<?php echo isset($row['id_producto']) ? $row['id_producto'] : ''; ?>"><br>
                <label for="nombre">Nombre: </label>
                <input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre"
                    value="<?php echo isset($row['nombre']) ? $row['nombre'] : ''; ?>"><br>
                <label for="descripcion">Descripcion: </label>
                <input type="text" name="descripcion" id="descripcion" placeholder="Ingresa una breve descripcion"
                    value="<?php echo isset($row['descripcion']) ? $row['descripcion'] : ''; ?>"><br>
                <label for="precio">Precio: </label>
                <input type="text" name="precio" id="precio" placeholder="Ingresa el precio"
                    value="<?php echo isset($row['precio']) ? $row['precio'] : ''; ?>"><br>
                <label for="fecha_venc">Fecha de vencimiento: </label>
                <input type="date" name="fecha_venc" id="fecha_venc" placeholder="Ingresa La fecha de vencimiento"
                    value="<?php echo isset($row['fecha_venc']) ? $row['fecha_venc'] : ''; ?>"><br>
                
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
