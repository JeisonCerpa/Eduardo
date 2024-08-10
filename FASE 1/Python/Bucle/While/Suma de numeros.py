sum = 0
while True:
    num = int(input("Ingresa un numero(numero 0 para detener): "))
    if num == 0:
        break
    sum += num
print("La suma de los numeros ingresados es:", sum)