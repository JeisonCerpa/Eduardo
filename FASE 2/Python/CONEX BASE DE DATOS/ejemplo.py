import mysql.connector

con =mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="empleados"
)
jei=con.cursor()
jei.execute("insert into empleados (nombre, apellido, puesto, salario, fecha_contratacion) values (%s, %s, %s, %s, %s)", ("Jesu", "Mendoza", "Desarrollador", 2000, "2023-09-01"))
con.commit()