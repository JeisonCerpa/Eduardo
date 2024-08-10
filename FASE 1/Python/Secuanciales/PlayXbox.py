pesoplay=2.3
pesox_box=3.2
costo_envio=5
playvendidos=int(input("Ingrese los PlayStation 5 vendidos: "))
xboxvendidos=int(input("Ingrese los Xbox Serie S vendidos: "))
pesopaquete=((playvendidos*2.3)+(xboxvendidos*3.2))
costototal=pesopaquete*costo_envio
print(f"El peso total de el paquete son: {pesopaquete} Libras")
print(f"El total del envio son: ${costototal}")