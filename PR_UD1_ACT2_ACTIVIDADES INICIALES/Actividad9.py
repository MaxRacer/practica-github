#Programa que pida los segundos y muestre por pantalla y en la misma frase 
# los minutos y las horas
var1=float(input("Introduce un número de segundos"))
total_horas=var1/3600
horas3decimales=round(total_horas, 3)
total_minutos=var1/60
minutos3decimales=round(total_minutos, 3)
print("El total de horas es", horas3decimales, "y el total de minutos es",
 minutos3decimales)
