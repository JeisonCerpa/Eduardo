#150kg en la cabina maximo, nombre y peso de los tripulantes, si se pasa de 150kg no se puede subir, 6 personas
from os import system
system("cls")
personas = []
pesos = []
while (len(personas) < 6):
    persona = input("Ingrese su nombre: ")
    peso = float(input("Ingrese su peso en Kg: "))
    personas.append(persona)
    pesos.append(peso)
print(f"Personas: {personas}")
pareja_encontrada = False
pareja_menor_peso = []
peso_menor = []
for i in range(len(pesos)):
    for j in range(i+1, len(pesos)):
        if pesos[i] + pesos[j] < 150:
            print(f"Pareja encontrada: {personas[i]} y {personas[j]}")
            print(f"Con un peso de {pesos[i]}kg y {pesos[j]}kg respectivamente.")
            print(f"Con un peso total de {pesos[i] + pesos[j]}kg.")
            pareja_encontrada = True
            if len(pareja_menor_peso) == 0:
                pareja_menor_peso = [personas[i], personas[j]]
                peso_menor = [pesos[i], pesos[j]]
            elif sum(peso_menor) > pesos[i] + pesos[j]:
                pareja_menor_peso = (personas[i], personas[j])
                peso_menor = pesos[i], pesos[j]
if pareja_encontrada == True:
    print(f"La pareja con menor peso total es: {pareja_menor_peso[0]} y {pareja_menor_peso[1]}")
    print(f"Con un peso total de {peso_menor}kg.")
if pareja_encontrada == False:
    print("No se encontró ninguna pareja con un peso total menor a 150kg.")