from os import system
system("cls")
tm = int(input("Digite el tamaño de la  matriz: "))
for i in range(tm):
    for j in range(tm):
        if i <= tm - j - 1:  # Invertir la condición de la diagonal
            print("1", end="  ")
        else:
            print("0", end="  ")
    print()
