import tkinter as tk
from tkinter import messagebox
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="gabineteabogados"
    )
    tablas = con.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error de conexión: {err}")
    exit(1)
    
root = tk.Tk()
root.title("Gestión de Usuarios")

tk.Label(root, text="DNI:").grid(row=0, column=0)
tk.Label(root, text="Nombre:").grid(row=1, column=0)
tk.Label(root, text="Dirección:").grid(row=2, column=0)

entry_dni = tk.Entry(root)
entry_nombre = tk.Entry(root)
entry_direccion = tk.Entry(root)

entry_dni.grid(row=0, column=1)
entry_nombre.grid(row=1, column=1)
entry_direccion.grid(row=2, column=1)

def consultar():
    dni = entry_dni.get()
    nombre = entry_nombre.get()
    direccion = entry_direccion.get()

    try:
        tablas.execute(
            "SELECT * FROM `procuradores` WHERE dni = %s;",
            (dni,)
        )
        cliente = tablas.fetchone()
        if cliente:
            entry_nombre.delete(0, tk.END)
            entry_direccion.delete(0, tk.END)
            entry_nombre.insert(0, cliente[1])
            entry_direccion.insert(0, cliente[2])
        else:
            messagebox.showwarning("Advertencia", "Cliente no encontrado.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al consultar: {err}")
        
tk.Button(root, text="Consultar", command=consultar).grid(row=3, column=0)

    
root.mainloop()