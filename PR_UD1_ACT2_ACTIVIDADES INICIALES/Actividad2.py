#Programa que introduzca por teclado tres tipos de variables y se muestren por pantalla
# en el siguiente orden: número entero, texto y número decimal
import time
número_entero=int(input("Introduzca un número entero"))
letra=input("Introduzca una letra cualquiera")
decimal=float(input("Introduzca un número decimal"))
print("El número entero que ha introducido es", número_entero)
time.sleep(1)
print("La letra que ha introducido es", letra)
time.sleep(1)
print("El número decimal que ha introducido es", decimal)