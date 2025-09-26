#Utiliza el valor Pi de la librería math para calcular 
# el área y volumen de un cilindro, introduciendo por teclado el valor
# de radio y altura. Resultado con 2 decimales.
import math
var1=float(input("Introduce el radio de un cilindro"))
var2=float(input("Introduce la altura de un cilindro"))
area=2*math.pi*var1*(var1+var2)
area_redondeada=round(area, 2)
volumen=math.pi*var1**2*var2
volumen_redondeado=round(volumen, 2)
print("El área de un cilindro es:", area_redondeada)
print("El volumen de un cilindro es:", volumen_redondeado)