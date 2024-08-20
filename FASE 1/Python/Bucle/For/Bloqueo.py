print('Ingrese el pin de ingreso')
for i in range (3,0,-1):
    pin=int(input(''))
    if pin == 3430:
        print("Ha ingresado correctamente")
        break
    else:
        print(f'Contrasena incorrecta, intentos restantes {i-1}')
if pin != 3430:
    print("Ha superado el numero de intentos permitidos")
    print('Llamando a la policia')