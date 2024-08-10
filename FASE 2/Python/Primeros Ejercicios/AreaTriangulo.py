import math
a = float(input("Digite el tamaño de el lado A: "))	
b = float(input("Digite el tamaño de el lado B:  "))
c = float(input("Digite el angulo θ: "))
c = math.radians(c)
area = (a*b*math.sin(c))/2
print (f"El area del triangulo es:  {round(area,2)}")

