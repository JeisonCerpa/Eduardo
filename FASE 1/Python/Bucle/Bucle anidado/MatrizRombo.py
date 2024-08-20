from os import system

system("cls")
tm = int(input("Digite el tamaño de la matriz: "))

for i in range(tm):
    for j in range(tm):
        distance = abs(i - tm // 2) + abs(j - tm // 2)
        if distance <= tm // 2:
            print("1", end=" ")
        else:
            print("0", end=" ")
    print()