<?php

// Obtener la elección del tipo de pizza y el ingrediente adicional
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
  echo "<p>**Tipo:** " . ($tipoPizza == "vegetariana" ? "Vegetariana" : "No Vegetariana") . "</p>";
  echo "<p>**Ingredientes:** Mozzarella, Tomate, " . $ingredienteElegido . "</p>";
}
