#Programa que pida un número de horas y muestre por pantalla los minutos 
# y segundo
import time
var1=int(input("Introduce un número de horas"))
total_minutos=var1*60
total_segundos=var1*3600
print("El total de minutos es", total_minutos)
time.sleep(1)
print("El total de segundos es", total_segundos)