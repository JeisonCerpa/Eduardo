nota = float(input("Introduce la nota: "))
if nota >= 0 and nota <= 10:
    if nota < 5:
        print("Suspenso")
    elif  5 <= nota < 7:
        print("Aprobado")
    elif  7 <= nota < 8.5:
        print("Notable")
    elif 8.5 <= nota < 10:
        print("Sobresaliente")
    elif nota == 10:
        print("Matrícula de honor")