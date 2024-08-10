import time
from os import system
import random
system("cls")
juego = ["Piedra", "Papel", "Tijeras"]
print("Bienvenido al juego de Piedra, Papel o Tijeras")
puntaje = 0
puntaje2 = 0
while(True):
    print(f"Tu puntaje es: {puntaje}")
    print(f"El puntaje de la computadora es: {puntaje2}")
    jugador = input("Ingresa tu elección (Piedra, Papel, Tijeras): ")
    computer = random.choice(juego)
    print(f"Escogiste: {jugador}")
    print(f"La computadora escogió: {computer}")
    if jugador == computer:
        print("Es un empate!")
    elif (jugador == "Piedra" and computer == "Tijeras") or \
         (jugador == "Papel" and computer == "Piedra") or \
         (jugador == "Tijeras" and computer == "Papel"):
        print("Ganaste!")
        puntaje += 1
        time.sleep(2)
        system("cls")
    else:
        print("La computadora ganó!")
        puntaje2 += 1
        time.sleep(2)
        system("cls")

