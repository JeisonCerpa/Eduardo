while(True):
    contra = input("Ingresa tu contraseña: ")
    contra2 = input("Confirma tu contraseña: ")
    if contra == contra2:
        print("Contraseña correcta")
        break
    else:
        print("Las contraseñas no coinciden")