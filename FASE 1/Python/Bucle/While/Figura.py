size = int(input("Ingrese el tamaño de la figura: "))
nivel = 1
while nivel <= size:
    asteriscos = '*' * (2 * nivel - 1)
    print(asteriscos)
    nivel += 1
while nivel >= 1:
    asteriscos = '*' * (2 * nivel - 1)
    print(asteriscos)
    nivel -= 1
