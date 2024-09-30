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
    system("cls")
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
            system("cls")
            print("Bienvenido al sistema de usuarios.")
            print("1. Consultar")
            print("2. Insertar")
            print("3. Reporte")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    print("---Consulta de usuarios---")
                    ingresar = input("Ingrese la cedula: ")
                    tablas.execute("SELECT * FROM `usuarios` WHERE cedula = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        system("cls")
                        print("---Consulta de usuarios---")
                        print(f"Cédula: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}, Dirección: {resultado[3]}, Teléfono: {resultado[4]}, Correo: {resultado[5]}, Contraseña: {resultado[6]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar usuario")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            system("cls")
                            print("---Actualización de usuarios---")
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
                    system("cls")
                    print("---Ingresar usuarios---")
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
            elif seleccion == 3:
                print("---Consulta de usuarios---")
                tablas.execute("SELECT * FROM `usuarios`")
                resultado = tablas.fetchall()
                for i in resultado:
                    print(f"Cédula: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, Dirección: {i[3]}, Teléfono: {i[4]}, Correo: {i[5]}, Contraseña: {i[6]}")
                input("Presione enter para continuar.")
            elif seleccion == 0:
                break
    elif seleccion == 2:
        while True:
            system("cls")
            print("Bienvenido al sistema de clientes.")
            print("1. Consultar")
            print("2. Insertar")
            print("3. Reporte")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    print("---Consulta de clientes---")
                    ingresar = input("Ingrese la cedula: ")
                    tablas.execute("SELECT * FROM `clientes` WHERE cedula = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        print(f"Cedula: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}, Direccion: {resultado[3]}, Telefono: {resultado[4]}, Email: {resultado[5]}") 
                        print("1. Para actualizar datos")
                        print("2. Para eliminar producto")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            cedula= input ('ingrese la cedula')
                            nombre = input("Ingrese el nombre: ")
                            apellidos = input("Ingrese un apellido: ")
                            direccion = input("Ingrese una direccion: ")
                            cedula = input("Ingrese su numero de cedula: ")
                            telefono = input("ingrese su numero de telefono:")
                            email = input("ingrese su email:")
                            tablas.execute("UPDATE `clientes` SET nombre = %s, apellido = %s, direccion = %s, cedula = %s, telefono = %s, email = %s, password = %s, WHERE cedula = %s;", (nombre, apellidos, direccion, cedula, telefono, email, ingresar))
                            con.commit()
                            print("Datos actualizados correctamente.")
                        elif opcion == "2":
                            tablas.execute("DELETE FROM `clientes` WHERE id_cliente = %s;", (ingresar,))
                            con.commit()
                            print("Usuario eliminado correctamente.")
                        elif opcion == "3":
                            continue
                        elif opcion == "0":
                            break
                    if ingresar == "0":
                            break
                    else:
                        print("No se encontró ningún producto con ese ID.")
            
            elif seleccion == 2:
                while True:
                    print("Ingrese los datos del usuario.")
                    cedula = input("Ingrese la cedula: ")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    telefono = input("Ingrese el telefono: ")
                    direccion = input("Ingrese la dirección: ")
                    email = input("Ingrese el email: ")
                    tablas.execute("INSERT INTO `clientes` (cedula, nombres, apellidos, direccion, telefono, email) VALUES (%s, %s, %s, %s, %s, %s);", (cedula, nombre, apellido, direccion, telefono, email))
                    con.commit()
                    print(" producto agregado correctamente.")
                    if input("¿Desea agregar otro producto? (s/n): ") == "n":
                        break
            elif seleccion == 3:
                print("---Consulta de clientes---")
                tablas.execute("SELECT * FROM `clientes`")
                resultado = tablas.fetchall()
                for i in resultado:
                    print(f"Cedula: {i[0]}, Nombre: {i[1]}, apellido: {i[2]}, direccion: {i[3]}, cedula: {i[4]} telefono: {i[5]} email: {i[6]}")
                input("Presione enter para continuar.")
            elif seleccion == 0:
                break
    elif seleccion == 3:
        while True:
            system("cls")
            print("Bienvenido al sistema de productos.")
            print("1. Consultar")
            print("2. Insertar")
            print("3. Reporte")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    system("cls")
                    print("----Consulta de productos----")
                    ingresar = input("Ingrese el ID del producto: ")
                    tablas.execute("SELECT * FROM `productos` WHERE id_producto = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        system("cls")
                        print("----Consulta de productos----")
                        print(f"ID del producto: {resultado[0]}, Nombre: {resultado[1]}, Descripcion: {resultado[2]}, Precio: {resultado[3]}, Fecha de Vencimiento: {resultado[4]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar producto")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            system("cls")
                            print("----Actualización de productos----")
                            nombre = input("Ingrese el nombre: ")
                            descripcion = input("Ingrese una breve descripcion: ")
                            precio = input("Ingrese el precio: ")
                            fecha_venc = input("Ingrese la fecha de vencimiento: ")
                            tablas.execute("UPDATE `productos` SET nombre = %s, descripcion = %s, precio = %s, fecha_venc = %s WHERE id_producto = %s;", (nombre, descripcion, precio, fecha_venc, ingresar))
                            con.commit()
                            print("Datos actualizados correctamente.")
                        elif opcion == "2":
                            system("cls")
                            tablas.execute("DELETE FROM `productos` WHERE id_producto = %s;", (ingresar,))
                            con.commit()
                            print("Usuario eliminado correctamente.")
                        elif opcion == "3":
                            continue
                        elif opcion == "0":
                            break
                    if ingresar == "0":
                            break
                    else:
                        print("No se encontró ningún producto con ese ID.")
            elif seleccion == 2:
                while True:
                    system("cls")
                    print("----Insertar productos----")
                    print("Ingrese los datos del usuario.")
                    id_producto = input("Ingrese la cédula: ")
                    nombre = input("Ingrese el nombre: ")
                    descripcion = input("Ingrese el apellido: ")
                    precio = input("Ingrese la dirección: ")
                    fecha_venc = input("Ingrese el teléfono: ")
                    tablas.execute("INSERT INTO `productos` (nombre, descripcion, precio, fecha_venc) VALUES (%s, %s, %s, %s);", (id_producto, nombre, descripcion, precio, fecha_venc))
                    con.commit()
                    print("Producto agregado correctamente.")
                    if input("¿Desea agregar otro producto? (s/n): ") == "n":
                        break
            elif seleccion == 3:
                print("---Consulta de productos---")
                tablas.execute("SELECT * FROM `productos`")
                resultado = tablas.fetchall()
                for i in resultado:
                    print(f"ID del producto: {i[0]}, Nombre: {i[1]}, Descripcion: {i[2]}, Precio: {i[3]}, Fecha de Vencimiento: {i[4]}")
                input("Presione enter para continuar.")
            elif seleccion == 0:
                break
    elif seleccion == 4:
        while True:
            system("cls")
            print("Bienvenido al sistema de categorias.")
            print("1. Consultar")
            print("2. Insertar")
            print("3. Reporte")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    system("cls")
                    print("---Consulta de categorias---")
                    ingresar = input("Ingrese el ID de la categoria: ")
                    tablas.execute("SELECT * FROM `categorias` WHERE id_categoria = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    
                    if resultado:
                        system("cls")
                        print("---Consulta de categorias---")
                        print(f"ID del categoria: {resultado[0]}, nombre: {resultado[1]}, descripcion: {resultado[2]}, num_producto: {resultado[3]}, imagen: {resultado[4]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar producto")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            system("cls")
                            print("---Actualización de categorias---")
                            nombre = input("Ingrese el nombre: ")
                            descripcion = input("Ingrese una breve descripcion: ")
                            num_producto = input("Ingrese el numero de productos: ")
                            imagen = input("Ingrese la url de la imagen: ")
                            tablas.execute("UPDATE `` SET nombre = %s, descripcion = %s, num_producto = %s, imagen = %s WHERE id_catalogo = %s;", (nombre, descripcion, num_producto, imagen, ingresar))
                            con.commit()
                            print("Datos actualizados correctamente.")
                        elif opcion == "2":
                            tablas.execute("DELETE FROM `categorias` WHERE id_categoria = %s;", (ingresar,))
                            con.commit()
                            print("Categoria eliminado correctamente.")
                        elif opcion == "3":
                            continue
                        elif opcion == "0":
                            break
                    if ingresar == "0":
                            break
                    else:
                        print("No se encontró ningúna categoria con ese ID.")
            elif seleccion == 2:
                while True:
                    system("cls")
                    print("---Insertar Categorias---")
                    print("Ingrese los datos de la categoria.")
                    nombre = input("Ingrese el nombre: ")
                    descripcion = input("Ingrese el apellido: ")
                    num_producto = input("Ingrese el numero del producto: ")
                    imagen = input("Ingrese el url de la imagen de la categoria: ")
                    tablas.execute("INSERT INTO `categorias` (nombre, descripcion, num_producto, imagen) VALUES (%s, %s, %s, %s);", (nombre, descripcion, num_producto, imagen))
                    con.commit()
                    print("Categoria agregado correctamente.")
                    if input("¿Desea agregar otra categoria? (s/n): ") == "n":
                        break
            elif seleccion == 3:
                print("---Consulta de categorias---")
                tablas.execute("SELECT * FROM `categorias`")
                resultado = tablas.fetchall()
                for i in resultado:
                    print(f"ID del categoria: {i[0]}, nombre: {i[1]}, descripcion: {i[2]}, num_producto: {i[3]}, imagen: {i[4]}")
                input("Presione enter para continuar.")        
            elif seleccion == 0:
                break
    elif seleccion == 5:
        while True:
            system("cls")
            print("Bienvenido al sistema de empleados.")
            print("1. Consultar")
            print("2. Insertar")
            print("3. Reporte")
            print("0. Salir")
            seleccion = int(input("Selecciona una opcion: "))
            if seleccion == 1:
                while True:
                    system("cls")
                    print("---Consulta de empleados---")
                    ingresar = input("Ingrese el ID del Empleado: ")
                    tablas.execute("SELECT * FROM `empleados` WHERE id_empleado = %s;", (ingresar,))
                    resultado = tablas.fetchone()
                    if resultado:
                        system("cls")
                        print("---Consulta de empleados---")
                        print(f"id_empleado: {resultado[0]}, Nombre: {resultado[1]}, Apellido: {resultado[2]}, correo_electronico: {resultado[3]}, Teléfono: {resultado[4]}, Cargo: {resultado[5]}, Salario: {resultado[6]}, Fecha de contratacion: {resultado[7]}")
                        print("1. Para actualizar datos")
                        print("2. Para eliminar Empleado")
                        print("3. Para volver a consultar")
                        print("0. Para salir")
                        opcion = input("Selecciona una opcion: ")
                        if opcion == "1":
                            system("cls")
                            print("---Actualización de empleados---")
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
                    system("cls")
                    print("---Ingresar empleados---")
                    print("Ingrese los datos del empleado.")
                    id_empleado = input("Ingrese el ID del empleado: ")
                    nombre = input("Ingrese el nombre: ")
                    apellido = input("Ingrese el apellido: ")
                    correo_electronico = input("Ingrese el  correo electronico: ")
                    telefono = input("Ingrese el teléfono: ")
                    cargo = input("Ingrese el cargo: ")
                    salario = input("Ingrese el salario: ")
                    fecha_contratacion = input("Ingrese la fecha de contratacion (AAAA-MM-DD): ")
                    tablas.execute("INSERT INTO `empleados` (nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);", (id_empleado, nombre, apellido, correo_electronico, telefono, cargo, salario, fecha_contratacion))
                    con.commit()
                    print("Empleado agregado correctamente.")
                    if input("¿Desea agregar otro Empleado? (s/n): ") == "n":
                        break
            elif seleccion == 3:
                print("---Consulta de empleados---")
                tablas.execute("SELECT * FROM `empleados`")
                resultado = tablas.fetchall()
                for i in resultado:
                    print(f"id_empleado: {i[0]}, Nombre: {i[1]}, Apellido: {i[2]}, correo_electronico: {i[3]}, Teléfono: {i[4]}, Cargo: {i[5]}, Salario: {i[6]}, Fecha de contratacion: {i[7]}")
                input("Presione enter para continuar.")        
            elif seleccion == 0:
                break
    elif seleccion == 0:
        break