from os import system

system("cls")
tm = int(input("Digite el tamaño de la matriz: "))
for i in range(tm):
    for j in range(tm):
        if i == tm // 2 or j == tm // 2:  # Verificar si estamos en la fila central o columna central
            print("1", end="  ")
        else:
            print("0", end="  ")
    print()
