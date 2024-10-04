import tkinter as tk
from tkinter import messagebox
import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="ejercicio"
    )
    tablas = con.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error de conexión: {err}")
    exit(1)
    
root = tk.Tk()
root.title("Gestión de Usuarios")

tk.Label(root, text="Cédula:").grid(row=0, column=0)
tk.Label(root, text="Nombre:").grid(row=1, column=0)
tk.Label(root, text="Apellido:").grid(row=2, column=0)
tk.Label(root, text="Dirección:").grid(row=3, column=0)
tk.Label(root, text="Teléfono:").grid(row=4, column=0)
tk.Label(root, text="Correo:").grid(row=5, column=0)
tk.Label(root, text="Contraseña:").grid(row=6, column=0)

entry_cedula = tk.Entry(root)
entry_nombre = tk.Entry(root)
entry_apellido = tk.Entry(root)
entry_direccion = tk.Entry(root)
entry_telefono = tk.Entry(root)
entry_correo = tk.Entry(root)
entry_contraseña = tk.Entry(root)

entry_cedula.grid(row=0, column=1)
entry_nombre.grid(row=1, column=1)
entry_apellido.grid(row=2, column=1)
entry_direccion.grid(row=3, column=1)
entry_telefono.grid(row=4, column=1)
entry_correo.grid(row=5, column=1)
entry_contraseña.grid(row=6, column=1)

def insertar_usuario():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()

    try:
        tablas.execute(
            "INSERT INTO `usuarios` (cedula, nombre, apellido, direccion, telefono, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s);",
            (cedula, nombre, apellido, direccion, telefono, correo, contraseña)
        )
        con.commit()
        messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al insertar: {err}")

def consultar_usuario():
    cedula = entry_cedula.get()
    tablas.execute("SELECT * FROM `usuarios` WHERE cedula = %s;", (cedula,))
    resultado = tablas.fetchone()

    if resultado:
        entry_nombre.delete(0, tk.END)
        entry_apellido.delete(0, tk.END)
        entry_direccion.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        entry_correo.delete(0, tk.END)
        entry_contraseña.delete(0, tk.END)

        entry_nombre.insert(0, resultado[1])
        entry_apellido.insert(0, resultado[2])
        entry_direccion.insert(0, resultado[3])
        entry_telefono.insert(0, resultado[4])
        entry_correo.insert(0, resultado[5])
        entry_contraseña.insert(0, resultado[6])
    else:
        messagebox.showwarning("Advertencia", "No se encontró ningún usuario con esa cédula.")

def actualizar_usuario():
    cedula = entry_cedula.get()
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    direccion = entry_direccion.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    contraseña = entry_contraseña.get()

    try:
        tablas.execute(
            "UPDATE `usuarios` SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s, password = %s WHERE cedula = %s;",
            (nombre, apellido, direccion, telefono, correo, contraseña, cedula)
        )
        con.commit()
        messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al actualizar: {err}")

def eliminar_usuario():
    cedula = entry_cedula.get()
    confirmacion = messagebox.askyesno("Confirmación", "¿Estás seguro que deseas eliminar este usuario?")
    if confirmacion:
        try:
            tablas.execute("DELETE FROM `usuarios` WHERE cedula = %s;", (cedula,))
            con.commit()
            messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al eliminar: {err}")

tk.Button(root, text="Insertar", command=insertar_usuario).grid(row=7, column=0)
tk.Button(root, text="Consultar", command=consultar_usuario).grid(row=7, column=1)
tk.Button(root, text="Actualizar", command=actualizar_usuario).grid(row=8, column=0)
tk.Button(root, text="Eliminar", command=eliminar_usuario).grid(row=8, column=1)

root.mainloop()

tablas.close()
con.close()
