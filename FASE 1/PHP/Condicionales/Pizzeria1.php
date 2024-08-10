<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pizzería Bella Napoli</title>
</head>
<body>
  <h1>Pizzería Bella Napoli</h1>
  <h2>¿Qué tipo de pizza deseas?</h2>
  <form action="Pizzeria1.php" method="post">
    <input type="submit" name="tipoPizza" value="Vegetariana" id="pizzaVegetariana">
    <input type="submit" name="tipoPizza" value="No Vegetariana" id="pizzaNoVegetariana">
  </form>
</body>
</html>
<?php   
// Definir los ingredientes
$ingredientesVegetarianos = array("Pimiento", "Tofu");
$ingredientesNoVegetarianos = array("Peperoni", "Jamón", "Salmón");

// Obtener la elección del tipo de pizza

   if (isset($_POST["tipoPizza"])) {
$tipoPizza = $_POST["tipoPizza"];
// Mostrar el menú y formulario para elegir ingrediente adicional

if ($tipoPizza != "") {
  echo "<h2>Elige un ingrediente adicional:</h2>";
  echo '<form action="Pizzeria1.php" method="post">';
  echo '<input type="hidden" name="tipoPizza" value="' . $tipoPizza . '">';

  if ($tipoPizza == "Vegetariana") {
    for ($i = 0; $i < count($ingredientesVegetarianos); $i++) {
      echo '<input type="radio" name="ingredienteElegido" value="' . $ingredientesVegetarianos[$i] . '" id="ingrediente' . $i . '">';
      echo '<label for="ingrediente' . $i . '">' . $ingredientesVegetarianos[$i] . '</label><br>';
    }
  } else {
    for ($i = 0; $i < count($ingredientesNoVegetarianos); $i++) {
      echo '<input type="radio" name="ingredienteElegido" value="' . $ingredientesNoVegetarianos[$i] . '" id="ingrediente' . $i . '">';
      echo '<label for="ingrediente' . $i . '">' . $ingredientesNoVegetarianos[$i] . '</label><br>';
    }
  }

  echo '<br>';
  echo '<input type="submit" value="Mostrar Pizza">';
  echo '</form>';
}
   }
   if (isset($_POST["tipoPizza"]) && isset($_POST["ingredienteElegido"])) {
    $tipoPizza = $_POST["tipoPizza"];
    $ingredienteElegido = $_POST["ingredienteElegido"];
  } else {
    $tipoPizza = "";
    $ingredienteElegido = "";
  }
  
  // Mostrar la pizza seleccionada
  if ($tipoPizza != "" && $ingredienteElegido != "") {
    echo "<h2>Tu pizza:</h2>";
    echo "<p>Tipo: " . ($tipoPizza == "vegetariana" ? "Vegetariana" : "No Vegetariana") . "</p>";
    echo "<p>Ingredientes: Mozzarella, Tomate, " . $ingredienteElegido . "</p>";
  }
  