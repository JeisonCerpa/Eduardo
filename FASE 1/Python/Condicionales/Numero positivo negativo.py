from os import system

system("cls")


print("     ██╗███████╗██╗███████╗ ██████╗ ███╗   ██╗     ██████╗███████╗██████╗ ██████╗  █████╗ ")
print("     ██║██╔════╝██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
print("     ██║█████╗  ██║███████╗██║   ██║██╔██╗ ██║    ██║     █████╗  ██████╔╝██████╔╝███████║")
print("██   ██║██╔══╝  ██║╚════██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║")
print("╚█████╔╝███████╗██║███████║╚██████╔╝██║ ╚████║    ╚██████╗███████╗██║  ██║██║     ██║  ██║")
print(" ╚════╝ ╚══════╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝")
n=float(input("Ingrese un número: "))
if n>0:
    print("El número es positivo")
elif n== 0:
    print("El número es 0")
else:
    print("El número es negativo")