peso=float(input("Ingrese su peso en kg: "))
estatura=float(input("Ingrese su estatura en metros: "))
imc=(peso)/(estatura)**2
if imc < 18.5:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, está bajo de peso.")
elif 18.5 <= imc < 25:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, su peso es adecuado.")
elif 25 <= imc < 30:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, está en sobre peso.")
elif 30 <= imc < 35:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, está en obesidad grado 1")
elif 35 <= imc < 40:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, está en obesidad grado 2")
else:
    print(f"Su indice de masa corporal es de: {round(imc,2)}, está en obesidad morbida")