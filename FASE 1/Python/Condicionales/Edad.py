
from os import system

system("cls")
print("     ██╗███████╗██╗███████╗ ██████╗ ███╗   ██╗     ██████╗███████╗██████╗ ██████╗  █████╗ ")
print("     ██║██╔════╝██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
print("     ██║█████╗  ██║███████╗██║   ██║██╔██╗ ██║    ██║     █████╗  ██████╔╝██████╔╝███████║")
print("██   ██║██╔══╝  ██║╚════██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║")
print("╚█████╔╝███████╗██║███████║╚██████╔╝██║ ╚████║    ╚██████╗███████╗██║  ██║██║     ██║  ██║")
print(" ╚════╝ ╚══════╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝")


edad=int(input("¿Cuál es tu edad?: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")