import tkinter as tk
import mysql.connector
from tkinter import messagebox
try:
    con = mysql.connector.connect(
        host="localhost", user="root", password="", database="gabineteabogados"
    )
    tablas = con.cursor()
except mysql.connector.Error as err:
    messagebox.showerror("Error", f"Error de conexión: {err}")
    exit(1)

def ventana_asuntos():
    ventana1 = tk.Toplevel()
    ventana1.title("Asuntos")
    ventana1.geometry("800x600")

    titulo = tk.Label(ventana1, text="Asuntos", font=("Arial", 20))
    titulo.grid(row=0, column=0, columnspan=4)
    ventana1.grid_columnconfigure(0, weight=1)
    ventana1.grid_columnconfigure(3, weight=1)

    tk.Label(ventana1, text="Número de Expediente:").grid(row=1, column=0)
    tk.Label(ventana1, text="DNI del Cliente:").grid(row=2, column=0)
    tk.Label(ventana1, text="Fecha de Inicio:").grid(row=3, column=0)
    tk.Label(ventana1, text="Fecha de Fin:").grid(row=4, column=0)
    tk.Label(ventana1, text="Estado:").grid(row=5, column=0)
    tk.Label(ventana1, text="Procurador:").grid(row=6, column=0)

    entry_n_expediente = tk.Entry(ventana1)
    entry_clientedni = tk.Entry(ventana1)
    entry_fecha_inicio = tk.Entry(ventana1)
    entry_fecha_fin = tk.Entry(ventana1)
    entry_Estado = tk.Entry(ventana1)
    entry_procurador = tk.Entry(ventana1)

    entry_n_expediente.grid(row=1, column=1)
    entry_clientedni.grid(row=2, column=1)
    entry_fecha_inicio.grid(row=3, column=1)
    entry_fecha_fin.grid(row=4, column=1)
    entry_Estado.grid(row=5, column=1)
    entry_procurador.grid(row=6, column=1)
    
    def insertar_asunto():
        n_expediente = entry_n_expediente.get()
        clientedni = entry_clientedni.get()
        fecha_inicio = entry_fecha_inicio.get()
        fecha_fin = entry_fecha_fin.get()
        estado = entry_Estado.get()
        procurador = entry_procurador.get()

        try:
            tablas.execute(
                "INSERT INTO `asuntos` (numero_expediente, cliente_dni, fecha_inicio, fecha_fin, estado) VALUES (%s, %s, %s, %s, %s);",
                (n_expediente, clientedni, fecha_inicio, fecha_fin, estado),
            )
            tablas.execute(
                "INSERT INTO `asuntos_procuradores` (numero_expediente, procurador_dni) VALUES (%s, %s);",
                (n_expediente, procurador),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al insertar: {err}")

    def consultar_asunto():
        n_expediente = entry_n_expediente.get()
        try:
            tablas.execute(
                "SELECT a.numero_expediente, a.cliente_dni, a.fecha_inicio, a.fecha_fin, a.estado, pa.procurador_dni "
                "FROM asuntos a "
                "LEFT JOIN procuradores_asuntos pa ON a.numero_expediente = pa.numero_expediente "
                "WHERE a.numero_expediente = %s;", 
                (n_expediente,)
            )
            resultado = tablas.fetchone()
            if resultado:
                entry_n_expediente.delete(0, tk.END)
                entry_clientedni.delete(0, tk.END)
                entry_fecha_inicio.delete(0, tk.END)
                entry_fecha_fin.delete(0, tk.END)
                entry_Estado.delete(0, tk.END)
                entry_procurador.delete(0, tk.END)
                
                entry_n_expediente.insert(0, resultado[0])
                entry_clientedni.insert(0, resultado[1])
                entry_fecha_inicio.insert(0, resultado[2])
                entry_fecha_fin.insert(0, resultado[3])
                entry_Estado.insert(0, resultado[4])
                entry_procurador.insert(0, resultado[5])
            else:
                messagebox.showwarning(
                    "Advertencia", "No se encontró ningún asunto con ese número de expediente."
                )
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al consultar: {err}")

    def actualizar_asunto():
        n_expediente = entry_n_expediente.get()
        clientedni = entry_clientedni.get()
        fecha_inicio = entry_fecha_inicio.get()
        fecha_fin = entry_fecha_fin.get()
        estado = entry_Estado.get()

        try:
            tablas.execute(
                "UPDATE `asuntos` SET cliente_dni = %s, fecha_inicio = %s, fecha_fin = %s, estado = %s WHERE numero_expediente = %s;",
                (n_expediente, clientedni, fecha_inicio, fecha_fin, estado),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar: {err}")

    def eliminar_asunto():
        n_expediente = entry_n_expediente.get()
        confirmacion = messagebox.askyesno(
            "Confirmación", "¿Estás seguro que deseas eliminar este usuario?"
        )
        if confirmacion:
            try:
                tablas.execute(
                    "DELETE FROM `asuntos` WHERE numero_expediente = %s;",
                    (n_expediente,),
                )
                con.commit()
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al eliminar: {err}")

    tk.Button(ventana1, text="Insertar", command=insertar_asunto).grid(row=7, column=0)
    tk.Button(ventana1, text="Consultar", command=consultar_asunto).grid(
        row=7, column=1
    )
    tk.Button(ventana1, text="Actualizar", command=actualizar_asunto).grid(
        row=8, column=0
    )
    tk.Button(ventana1, text="Eliminar", command=eliminar_asunto).grid(row=8, column=1)

    ventana1.mainloop()


def ventana_clientes():
    ventana2 = tk.Toplevel()
    ventana2.title("Clientes")
    ventana2.geometry("800x600")

    titulo = tk.Label(ventana2, text="Clientes", font=("Arial", 20))
    titulo.grid(row=0, column=0, columnspan=4)
    ventana2.grid_columnconfigure(0, weight=1)
    ventana2.grid_columnconfigure(3, weight=1)
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="gabineteabogados"
        )
        tablas = con.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error de conexión: {err}")
        exit(1)

    tk.Label(ventana2, text="DNI:").grid(row=1, column=0)
    tk.Label(ventana2, text="Nombre:").grid(row=2, column=0)
    tk.Label(ventana2, text="Dirección:").grid(row=3, column=0)
    tk.Label(ventana2, text="Email:").grid(row=4, column=0)
    tk.Label(ventana2, text="Teléfono:").grid(row=5, column=0)

    entry_dni = tk.Entry(ventana2)
    entry_nombre = tk.Entry(ventana2)
    entry_direccion = tk.Entry(ventana2)
    entry_email = tk.Entry(ventana2)
    entry_telefono = tk.Entry(ventana2)

    entry_dni.grid(row=1, column=1)
    entry_nombre.grid(row=2, column=1)
    entry_direccion.grid(row=3, column=1)
    entry_email.grid(row=4, column=1)
    entry_telefono.grid(row=5, column=1)

    def insertar_cliente():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        email = entry_email.get()
        telefono = entry_telefono.get()

        try:
            tablas.execute(
                "INSERT INTO `clientes` (dni, nombre, direccion, email, telefono) VALUES (%s, %s, %s, %s, %s);",
                (dni, nombre, direccion, email, telefono),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al insertar: {err}")

    def consultar_cliente():
        dni = entry_dni.get()
        tablas.execute("SELECT * FROM `clientes` WHERE dni = %s;", (dni,))
        resultado = tablas.fetchone()

        if resultado:
            entry_dni.delete(0, tk.END)
            entry_nombre.delete(0, tk.END)
            entry_direccion.delete(0, tk.END)
            entry_email.delete(0, tk.END)
            entry_telefono.delete(0, tk.END)
            
            entry_dni.insert(0, resultado[0])
            entry_nombre.insert(0, resultado[1])
            entry_direccion.insert(0, resultado[2])
            entry_email.insert(0, resultado[3])
            entry_telefono.insert(0, resultado[4])
        else:
            messagebox.showwarning(
                "Advertencia", "No se encontró ningún usuario con esa cédula."
            )

    def actualizar_cliente():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()
        email = entry_email.get()
        telefono = entry_telefono.get()

        try:
            tablas.execute(
                "UPDATE `clientes` SET nombre = %s, direccion = %s, email = %s, telefono = %s WHERE dni = %s;",
                (nombre, direccion, email, telefono, dni),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar: {err}")

    def eliminar_cliente():
        dni = entry_dni.get()
        confirmacion = messagebox.askyesno(
            "Confirmación", "¿Estás seguro que deseas eliminar este usuario?"
        )
        if confirmacion:
            try:
                tablas.execute("DELETE FROM `clientes` WHERE dni = %s;", (dni,))
                con.commit()
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al eliminar: {err}")

    tk.Button(ventana2, text="Insertar", command=insertar_cliente).grid(row=6, column=0)
    tk.Button(ventana2, text="Consultar", command=consultar_cliente).grid(
        row=6, column=1
    )
    tk.Button(ventana2, text="Actualizar", command=actualizar_cliente).grid(
        row=7, column=0
    )
    tk.Button(ventana2, text="Eliminar", command=eliminar_cliente).grid(row=7, column=1)

    ventana2.mainloop()


def ventana_procuradores():
    ventana3 = tk.Toplevel()
    ventana3.title("Procuradores")
    ventana3.geometry("800x600")

    titulo = tk.Label(ventana3, text="Procuradores", font=("Arial", 20))
    titulo.grid(row=0, column=0, columnspan=4)
    ventana3.grid_columnconfigure(0, weight=1)
    ventana3.grid_columnconfigure(3, weight=1)
    try:
        con = mysql.connector.connect(
            host="localhost", user="root", password="", database="gabineteabogados"
        )
        tablas = con.cursor()
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error de conexión: {err}")
        exit(1)

    tk.Label(ventana3, text="DNI:").grid(row=1, column=0)
    tk.Label(ventana3, text="Nombre:").grid(row=2, column=0)
    tk.Label(ventana3, text="Dirección:").grid(row=3, column=0)

    entry_dni = tk.Entry(ventana3)
    entry_nombre = tk.Entry(ventana3)
    entry_direccion = tk.Entry(ventana3)

    entry_dni.grid(row=1, column=1)
    entry_nombre.grid(row=2, column=1)
    entry_direccion.grid(row=3, column=1)

    def insertar_procurador():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()

        try:
            tablas.execute(
                "INSERT INTO `procuradores` (dni, nombre, direccion) VALUES (%s, %s, %s);",
                (dni, nombre, direccion),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario agregado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al insertar: {err}")

    def consultar_procurador():
        dni = entry_dni.get()
        try:
            tablas.execute(
                "SELECT * FROM `procuradores` WHERE dni = %s;", (dni,)
            )
            resultado = tablas.fetchone()
            if resultado:
                entry_dni.delete(0, tk.END)
                entry_nombre.delete(0, tk.END)
                entry_direccion.delete(0, tk.END)
                entry_dni.insert(0, resultado[0])
                entry_nombre.insert(0, resultado[1])
                entry_direccion.insert(0, resultado[2])
            else:
                messagebox.showwarning(
                    "Advertencia", "No se encontró ningún procurador con ese DNI."
                )
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al consultar: {err}")

    def actualizar_procurador():
        dni = entry_dni.get()
        nombre = entry_nombre.get()
        direccion = entry_direccion.get()

        try:
            tablas.execute(
                "UPDATE `procuradores` SET nombre = %s, direccion = %s WHERE dni = %s;",
                (nombre, direccion, dni),
            )
            con.commit()
            messagebox.showinfo("Éxito", "Usuario actualizado correctamente.")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error al actualizar: {err}")

    def eliminar_procurador():
        dni = entry_dni.get()
        confirmacion = messagebox.askyesno(
            "Confirmación", "¿Estás seguro que deseas eliminar este usuario?"
        )
        if confirmacion:
            try:
                tablas.execute("DELETE FROM `procuradores` WHERE dni = %s;", (dni,))
                con.commit()
                messagebox.showinfo("Éxito", "Usuario eliminado correctamente.")
            except mysql.connector.Error as err:
                messagebox.showerror("Error", f"Error al eliminar: {err}")

    tk.Button(ventana3, text="Insertar", command=insertar_procurador).grid(
        row=6, column=0
    )
    tk.Button(ventana3, text="Consultar", command=consultar_procurador).grid(
        row=6, column=1
    )
    tk.Button(ventana3, text="Actualizar", command=actualizar_procurador).grid(
        row=7, column=0
    )
    tk.Button(ventana3, text="Eliminar", command=eliminar_procurador).grid(
        row=7, column=1
    )

    ventana3.mainloop()

root = tk.Tk()
root.title("Gabinete de Abogados")
root.geometry("800x600")

titulo = tk.Label(root, text="Gabinete de Abogados", font=("Arial", 20))
titulo.grid(row=0, column=0, columnspan=4)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(3, weight=1)

asuntos = tk.Button(
    root,
    text="Asuntos",
    command=ventana_asuntos,
    font=("Arial", 12),
    width=20,
    height=1,
)
asuntos.grid(row=1, column=0, pady=30, padx=40)

clientes = tk.Button(
    root,
    command=ventana_clientes,
    text="Clientes",
    font=("Arial", 12),
    width=20,
    height=1,
)
clientes.grid(row=1, column=1, pady=10)

procuradores = tk.Button(
    root,
    command=ventana_procuradores,
    text="Procuradores",
    font=("Arial", 12),
    width=20,
    height=1,
)
procuradores.grid(row=1, column=2, pady=10, padx=40)

root.mainloop()
