""" class Perro:
    # Atributo de clase
    especie = 'mamífero'

    # El método __init__ es llamado al crear el objeto
    def __init__(self, nombre, raza):
        print(f"Creando perro {nombre}, {raza}")

        # Atributos de instancia
        self.nombre = nombre
        self.raza = raza

    def ladra(self):
        print("Guau")

    def camina(self, pasos):
        print(f"Caminando {pasos} pasos")
        
mi_perro = Perro("Toby", "Bulldog")
mi_perro.ladra()
mi_perro.camina(10) """

def suma (a, b):
    return a + b

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))

sumar = suma(a, b)

print(sumar)