# Realiza un programa que a partir de introducir el diámetro de un 
# círculo calcule el área y perímetro. Importa la librería match y
# utiliza el valor PI para hacer el cálculo. Redondea el 
# resultado a un decimal
import math
var1=float(input("Introduce el diámetro de un círculo"))
perimetro=math.pi*var1
radio=var1/2
area=math.pi*radio**2
perimetro_redondeado=round(perimetro, 1)
area_redondeando=round(area, 1)
print("El perímetro del círculo es:", perimetro_redondeado)
print("El área del círculo es:", area_redondeando)
