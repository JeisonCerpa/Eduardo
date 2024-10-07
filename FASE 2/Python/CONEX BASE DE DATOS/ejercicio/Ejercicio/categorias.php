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
            $id_categoria = $_POST['id_categoria'];
            // Verifica si se ingresó un ID válido
            if (!empty($id_categoria)) {
                // Evitar inyección SQL con mysqli_real_escape_string
                $id_categoria = mysqli_real_escape_string($conectar, $id_categoria);

                // Realiza la consulta
                $query = "SELECT * FROM categorias WHERE id_categoria = '$id_categoria'";
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
                $id_categoria = $_POST['id_categoria'];
                $nombre = $_POST['nombre'];
                $descripcion = $_POST['descripcion'];
                $num_producto = $_POST['num_producto'];
                $imagen = $_POST['imagen'];

                // Preparar la consulta
                $sql = "INSERT INTO categorias (id_categoria, nombre, descripcion, num_producto, imagen) VALUES (?, ?, ?, ?, ?)";

                $stmt = $conectar->prepare($sql);
                $stmt->bind_param("sssss", $id_categoria, $nombre, $descripcion, $num_producto, $imagen);

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
                $mensaje = "<script>alert('Por favor, complete el formulario.');</script>";
            }

            break;

            case 'Eliminar':
                $id_categoria = $_POST['id_categoria'];
                if (!empty($id_categoria)) {
                    $query = "DELETE FROM categorias WHERE id_categoria = '$id_categoria'";
                    $result = mysqli_query($conectar, $query);
                    if ($result) {
                        echo "<script>alert('Registro eliminado.');</script>";
                    } else {
                        echo "<script>alert('Error al eliminar el registro.');</script>";
                    }
                }
                break;

        case 'Actualizar':
                $id_categoria = $_POST['id_categoria'];
                $nombre = $_POST['nombre'];
                $descripcion = $_POST['descripcion'];
                $num_producto = $_POST['num_producto'];
                $imagen = $_POST['imagen'];

            $id_categoria = mysqli_real_escape_string($conectar, $id_categoria);
            $nombre = mysqli_real_escape_string($conectar, $nombre);
            $descripcion = mysqli_real_escape_string($conectar, $descripcion);
            $num_producto = mysqli_real_escape_string($conectar, $num_producto);
            $imagen = mysqli_real_escape_string($conectar, $imagen);

            $query = 
            "UPDATE categorias 
            SET nombre = '$nombre', 
            descripcion = '$descripcion', 
            num_producto = '$num_producto', 
            imagen = '$imagen' 
            WHERE id_categoria = '$id_categoria'";

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
    <title>Categorias</title>
    <link rel="stylesheet" href="CSS/style.css">
</head>

<body>
    <h1>Datos de las Categorias</h1>
    <section>
        <div class="title"><h2> Ingresa los datos </h2></div>
        <div class="usuarios">
            <form action="categorias.php" method="POST">
            <label for="nombre">ID Categoria: </label>
                <input type="text" name="id_categoria" id="id_categoria" placeholder="Ingresa el ID del producto"
                    value="<?php echo isset($row['id_categoria']) ? $row['id_categoria'] : ''; ?>"><br>

                <label for="nombre">Nombre: </label>
                <input type="text" name="nombre" id="nombre" placeholder="Ingresa el nombre"
                    value="<?php echo isset($row['nombre']) ? $row['nombre'] : ''; ?>"><br>

                <label for="descripcion">Descripcion: </label>
                <input type="text" name="descripcion" id="descripcion" placeholder="Ingresa la descripción"
                    value="<?php echo isset($row['descripcion']) ? $row['descripcion'] : ''; ?>"><br>

                <label for="num_prducto">Numero de producto: </label>
                <input type="number" name="num_producto" id="num_producto" placeholder="Numero del producto"
                    value="<?php echo isset($row['num_producto']) ? $row['num_producto'] : ''; ?>"><br>

                <label for="imagen">Url de la imagen: </label>
                <input type="text" name="imagen" id="imagen" placeholder="Ingresa la url de la imagen"
                    value="<?php echo isset($row['imagen']) ? $row['imagen'] : ''; ?>"><br>

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
