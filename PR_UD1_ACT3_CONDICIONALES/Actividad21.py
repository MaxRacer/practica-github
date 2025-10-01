# Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz 
# cuadrada no de un valor negativo
import math
a=int(input("¿Cuál es el valor a?"))
b=int(input("¿Cuál es el valor b?"))
c=int(input("¿Cuál es el valor c?"))
raiz=b**2-4*a*c
if raiz<0:
    print("La ecuación no tiene solución real")
else:
    resultado_positivo=(-b+math.sqrt(raiz))/2*a
    resultados_negativo=(-b-math.sqrt(raiz))/2*a
    print("El valor de x1 es:", resultado_positivo)
    print("El valor de x2 es:", resultados_negativo)