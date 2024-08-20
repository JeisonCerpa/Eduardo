from os import system

system("cls")
tm = int(input("Digite el tamaño de la matriz: "))
for i in range(tm):
    for j in range(tm):
        if i == 0 or i == tm - 1 or j == 0 or j == tm - 1:  # Verificar si estamos en el borde de la matriz
            print("1", end="  ")
        else:
            print("0", end="  ")
    print()
