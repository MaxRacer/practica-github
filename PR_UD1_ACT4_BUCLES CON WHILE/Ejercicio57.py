#Realiza un programa que permita adivinar un número comprendido entre 1 y 5. El programa 
# debe controlar si el usuario introduce un número no comprendido entre 1 y 5.
import random
numero = random.randint(1, 5)  
numero_usuario = int(input("Introduce un número entre 1 y 5: "))

while 1<= numero_usuario <= 5:   
    if numero_usuario == numero:
        print("¡Número acertado!")
        break
    else:
        print("Número no acertado, intenta de nuevo.")
        numero_usuario = int(input("Introduce un número entre 1 y 5: "))

print("Fin del programa")