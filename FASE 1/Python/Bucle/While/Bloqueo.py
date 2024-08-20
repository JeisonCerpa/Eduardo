
intento=0
while intento <= 3:
    pin = int(input("Ingrese su PIN: "))
    if pin == 1234:
        print("PIN correcto")
        break
    else:
        print("PIN incorrecto")
        print("Intento", intento, "de 3")
        intento+=1
if intento >= 3:
    print("Maximos intentos alcanzados")
    print("Celular blqueado")


