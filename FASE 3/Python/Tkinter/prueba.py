import tkinter as tk
from tkinter import ttk
import mysql.connector

# Conexión a la base de datos MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="tu_usuario",
    password="tu_contraseña",
    database="tu_base_de_datos"
)

# Crear la ventana principal
root = tk.Tk()
root.title("Combobox con datos de la base de datos")
root.geometry("300x200")

# Función para obtener datos de la base de datos
def obtener_datos():
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre_producto FROM productos")  # Cambia esta consulta según tu tabla y columna
    resultados = cursor.fetchall()
    cursor.close()
    return [fila[0] for fila in resultados]

# Crear el Combobox y llenarlo con los datos
valores = obtener_datos()
combobox = ttk.Combobox(root, values=valores)
combobox.pack(pady=20)

# Función para manejar la selección en el Combobox
def seleccion():
    print("Has seleccionado:", combobox.get())

# Botón para mostrar la selección actual
boton = tk.Button(root, text="Seleccionar", command=seleccion)
boton.pack(pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()

# Cerrar la conexión a la base de datos al finalizar
conexion.close()
