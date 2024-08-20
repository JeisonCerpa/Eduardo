nivel = 1
altura = int(input('Ingrese la altura de la pirámide: '))

while nivel <= altura:
  espacios = ' ' * (altura - nivel)
  asteriscos = '*' * (2 * nivel - 1)
  print(espacios + asteriscos)

  nivel += 1
print(' ' * (altura - 2) + '|' + '|'+ '|') 