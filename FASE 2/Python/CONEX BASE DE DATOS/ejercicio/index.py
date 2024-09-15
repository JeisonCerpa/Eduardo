from os import system
import mysql.connector
system("cls")
con =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ejercicio"
)

tablas = con.cursor()
while True:
    print("Bienvenido al sistema de gestion de base de datos.")
    print("1. Usuarios")
    print("2. Clientes")
    print("3. Productos")
    print("4. Categorias")
    print("5. Empleados")
    print("0. Salir")
    seleccion = int(input("Selecciona una opcion: "))
    if seleccion == 1:
        while True:
            print("Bienvenido al sistema de usuarios.")
            print("1. Consultar")
            print("2. Insertar")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    ingresar = input("Ingrese la cedula: ")
                    tablas.execute("SELECT * FROM `usuarios` WHERE cedula = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        print(f"Cédula: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}, Dirección: {resultado[3]}, Teléfono: {resultado[4]}, Correo: {resultado[5]}, Contraseña: {resultado[6]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar usuario")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            nombre = input("Ingrese el nombre: ")
                            apellido = input("Ingrese el apellido: ")
                            direccion = input("Ingrese la dirección: ")
                            telefono = input("Ingrese el teléfono: ")
                            correo = input("Ingrese el correo: ")
                            contraseña = input("Ingrese la contraseña: ")
                            tablas.execute("UPDATE `usuarios` SET nombre = %s, apellido = %s, direccion = %s, telefono = %s, email = %s, password = %s WHERE cedula = %s;", (nombre, apellido, direccion, telefono, correo, contraseña, ingresar))
                            con.commit()
                            print("Datos actualizados correctamente.")
                        elif opcion == "2":
                            tablas.execute("DELETE FROM `usuarios` WHERE cedula = %s;", (ingresar,))
                            con.commit()
                            print("Usuario eliminado correctamente.")
                        elif opcion == "3":
                            continue
                        elif opcion == "0":
                            break
                    if ingresar == "0":
                            break
                    else:
                        print("No se encontró ningún usuario con esa cédula.")
            
            elif seleccion == 2:
                while True:
                    print("Ingrese los datos del usuario.")
                    cedula = input("Ingrese la cédula: ")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    direccion = input("Ingrese la dirección: ")
                    telefono = input("Ingrese el teléfono: ")
                    correo = input("Ingrese el correo: ")
                    contraseña = input("Ingrese la contraseña: ")
                    tablas.execute("INSERT INTO `usuarios` (cedula, nombre, apellido, direccion, telefono, email, password) VALUES (%s, %s, %s, %s, %s, %s, %s);", (cedula, nombre, apellido, direccion, telefono, correo, contraseña))
                    con.commit()
                    print("Usuario agregado correctamente.")
                    if input("¿Desea agregar otro usuario? (s/n): ") == "n":
                        break
            elif seleccion == 0:
                break
    elif seleccion == 2:
        break
    elif seleccion == 3:
        break
    elif seleccion == 4:
        break
    elif seleccion == 5:
        while True:
            print("Bienvenido al sistema de empleados.")
            print("1. Consultar")
            print("2. Insertar")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    ingresar = input("Ingrese el ID del Empleado: ")
                    tablas.execute("SELECT * FROM `empleados` WHERE id_empleado = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        print(f"id_empleado: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}, correo_electronico: {resultado[3]}, Teléfono: {resultado[4]}, Cargo: {resultado[5]}, Salario: {resultado[6]}, Fecha de contratacion: {resultado[7]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar Empleado")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            nombre = input("Ingrese el nombre: ")
                            apellido = input("Ingrese el apellido: ")
                            correo_electronico = input("Ingrese el correo electronico: ")
                            telefono = input("Ingrese el teléfono: ")
                            cargo = input("Ingrese el cargo: ")
                            salario = input("Ingrese el salario: ")
                            fecha_contratacion = input("Ingrese la fecha de contratacion (AAAA-MM-DD): ")
                            tablas.execute("UPDATE `empleados` SET nombre = %s, apellido = %s, correo_electronico = %s, telefono = %s, cargo = %s, salario = %s, fecha_contratacion = %s WHERE id_empleado = %s;", (nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion, ingresar))
                            con.commit()
                            print("Datos actualizados correctamente.")
                        elif opcion == "2":
                            tablas.execute("DELETE FROM `empleados` WHERE id_empleado = %s;", (ingresar,))
                            con.commit()
                            print("Empleado eliminado correctamente.")
                        elif opcion == "3":
                            continue
                        elif opcion == "0":
                            break
                    if ingresar == "0":
                            break
                    else:
                        print("No se encontró ningún empleado con esa ID.")
            
            elif seleccion == 2:
                while True:
                    print("Ingrese los datos del empleado.")
                    id_empleado = input("Ingrese el ID del empleado: ")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    correo_electronico = input("Ingrese el  correo electronico: ")
                    telefono = input("Ingrese el teléfono: ")
                    cargo = input("Ingrese el cargo: ")
                    salario = input("Ingrese el salario: ")
                    fecha_contratacion = input("Ingrese la fecha de contratacion (AAAA-MM-DD): ")
                    tablas.execute("INSERT INTO `empleados` (id_empleado, nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_empleado, nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion))
                    con.commit()
                    print("Empleado agregado correctamente.")
                    if input("¿Desea agregar otro Empleado? (s/n): ") == "n":
                        break
            elif seleccion == 0:
                break
    elif seleccion == 0:
        break