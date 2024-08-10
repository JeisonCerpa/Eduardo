#5 hombres, 5 mujeres, escogidos aleatoriamente por parejas
from os import system
import random
system("cls")
lista_hombres = []
lista_mujeres = []
for i in range(5):
    hombre = input("Nombre de hombre: ")
    lista_hombres.append(hombre)
for i in range(5):
    mujer = input("Nombre de mujer: ")
    lista_mujeres.append(mujer)
print(f"Lista de hombres: {lista_hombres}")
print(f"Lista de mujeres: {lista_mujeres}")
amigo_secreto = []
for i in range(5):
    hombre = random.choice(lista_hombres)
    mujer = random.choice(lista_mujeres)
    amigo_secreto.append((hombre, mujer))
    lista_hombres.remove(hombre)
    lista_mujeres.remove(mujer)
for i in amigo_secreto:
    print(i)
