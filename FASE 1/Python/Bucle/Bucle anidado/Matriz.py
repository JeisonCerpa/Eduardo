from os import system 
system("cls")
tm = int(input("Digite el tamaño de la  matriz: "))
system("cls")
for i in range(tm):
    for j in range(tm):
        if i == j:
            print("1", end="  ")
        else:
            print("0", end="  ")
    print()