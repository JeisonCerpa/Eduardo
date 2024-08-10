#10 personas, calificando servicio de 1 - 5, mostrar promedio
from os import system
system("cls")
personas = []
calificaciones = []
opciones = [1,2,3,4,5]
while(len(personas) < 10):
    persona = input("Nombre de la persona: ")
    calificacion = int(input("Calificación del servicio (1 - 5): "))
    if calificacion in opciones:
        personas.append(persona)
        calificaciones.append(calificacion)    
    else:
        print("Calificación no válida")
print(f"Personas: {personas}")
print(f"Calificaciones: {calificaciones}")
suma = 0
for i in calificaciones:
    suma += i
promedio = suma / len(calificaciones)
print(f"El promedio de calificaciones es: {promedio}")