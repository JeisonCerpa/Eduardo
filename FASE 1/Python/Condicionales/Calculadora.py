from os import system

system("cls")


print("     ██╗███████╗██╗███████╗ ██████╗ ███╗   ██╗     ██████╗███████╗██████╗ ██████╗  █████╗ ")
print("     ██║██╔════╝██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
print("     ██║█████╗  ██║███████╗██║   ██║██╔██╗ ██║    ██║     █████╗  ██████╔╝██████╔╝███████║")
print("██   ██║██╔══╝  ██║╚════██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║")
print("╚█████╔╝███████╗██║███████║╚██████╔╝██║ ╚████║    ╚██████╗███████╗██║  ██║██║     ██║  ██║")
print(" ╚════╝ ╚══════╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝")
print("                                                                                          ")
print("Calculadora Básica")
print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
print("5. Salir")
opcion = int(input("Selecciona una opción: "))
if opcion == 5:   
    print("Ha salido de la calculadora, gracias por usarla.")
elif 1<=opcion<=5:
    n1=int(input("Ingresa el primer número: "))
    n2=int(input("Ingresa el segundo número: "))
    if opcion == 1:
        print(f"El resultado de la suma es: {n1+n2}")
    elif opcion == 2:
        print(f"El resultado de la resta es: {n1-n2}")
    elif opcion == 3:
        print(f"El resultado de la multiplicación es: {n1*n2}")
    elif opcion == 4:
        if n2 == 0:
            print("La división por 0 no es permitida.")
        else:
            print(f"El resultado de la división es: {n1/n2}")
else:
    print("El número no está en la lista:")            