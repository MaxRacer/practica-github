# Diseña un programa que “piense” un numero aleatorio entre 0 y 1000 para que nos pida que 
#intentemos adivinarlo. En cada intento, el programa nos dirá si el numero introducido es mayor o 
#menor del correcto. No utilices break para salir del bucle. Cuando se acierte el número debe 
#mostrarse por pantalla un mensaje y el número de intentos.
import random
numero_secreto=random.randint(0, 1000)
numero=0
intentos=0
while numero!=numero_secreto:
    numero=int(input("Introduce un número: "))
    if numero_secreto>numero:
        intentos=intentos+1
        print("El número es mayor")
    if numero_secreto<numero:
        intentos=intentos+1
        print("El número es menor")
else:
    print(f"Acertaste, has realizado {intentos} intentos")
