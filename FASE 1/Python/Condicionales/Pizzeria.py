from os import system

system("cls")
print("     ██╗███████╗██╗███████╗ ██████╗ ███╗   ██╗     ██████╗███████╗██████╗ ██████╗  █████╗ ")
print("     ██║██╔════╝██║██╔════╝██╔═══██╗████╗  ██║    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗")
print("     ██║█████╗  ██║███████╗██║   ██║██╔██╗ ██║    ██║     █████╗  ██████╔╝██████╔╝███████║")
print("██   ██║██╔══╝  ██║╚════██║██║   ██║██║╚██╗██║    ██║     ██╔══╝  ██╔══██╗██╔═══╝ ██╔══██║")
print("╚█████╔╝███████╗██║███████║╚██████╔╝██║ ╚████║    ╚██████╗███████╗██║  ██║██║     ██║  ██║")
print(""" ╚════╝ ╚══════╝╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝     ╚═════╝╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝  ╚═╝
      
      
      
      """)

print(" _______  _______  ___      ___      _______    __    _  _______  _______  _______  ___      ___  ")
print("|  _    ||       ||   |    |   |    |   _   |  |  |  | ||   _   ||       ||       ||   |    |   | ")
print("| |_|   ||    ___||   |    |   |    |  |_|  |  |   |_| ||  |_|  ||    _  ||   _   ||   |    |   | ")
print("|       ||   |___ |   |    |   |    |       |  |       ||       ||   |_| ||  | |  ||   |    |   | ")
print("|  _   | |    ___||   |___ |   |___ |       |  |  _    ||       ||    ___||  |_|  ||   |___ |   | ")
print("| |_|   ||   |___ |       ||       ||   _   |  | | |   ||   _   ||   |    |       ||       ||   | ")
print("""|_______||_______||_______||_______||__| |__|  |_|  |__||__| |__||___|    |_______||_______||___| 
      """)
print("Seleccione su pizza: ")
print ("[1]. Pizza no vegetariana   [2]. Pizza Vegetariana")
select=int(input("Seleccione su pizza: "))
if select == 1:
    print("¿Qué proteina quiere?:")
    proteina=int(input(" 1. Peperoni  2. Jamón   3. Salmón -> "))
    if proteina == 1:
        print("Su pizza sería de Peperoni, con queso mozarella y tomate")
    elif proteina == 2:
        print("Su pizza sería de Jamón, con queso mozarella y tomate")
    elif proteina == 3:
        print("Su pizza sería de Salmón, con queso mozarella y tomate")
    else:
        print("El número seleccionado no está en la lista")
elif select == 2:
    print("¿Qué vegetales quiere?")
    vegetales=int(input("1. Pimientos  2. Tofu. -> "))
    if vegetales == 1:
        print("Su pizza sería de Pimientos, con queso mozarella y tomate")
    elif vegetales == 2:
        print("Su pizza sería de Tofu, con queso mozarella y tomate")
    else:
        print("El número seleccionado no está en la lista")
else:
    print("El número seleccionado no está en la lista")        