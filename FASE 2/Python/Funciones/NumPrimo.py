#Desarrolle un programa que utilize funciones para saber si un numero es primo o no.
from os import system
system("cls")
def primo(numero):
    if numero <= 3:
        return True
    elif numero % 2 == 0:
        return False
    else:
        return True
while(True):
    num = int(input("Ingrese un numero: "))
    print("Ingrese el numero 0 para salir")
    system("cls")
    if num < 1:
        print("Ingrese un numero positivo")
    elif primo(num) == True:
        print("El numero es primo")
    elif num == 0:
        break
    else:
        print("El numero no es primo")
