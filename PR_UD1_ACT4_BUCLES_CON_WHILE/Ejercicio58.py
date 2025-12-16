#Modifica el programa anterior para que tengas 3 intentos. Utiliza while
import random
numero = random.randint(1, 5)  
intentos=3
while intentos>0:
    numero_usuario = int(input("Introduce un número entre 1 y 5: "))
    if numero_usuario < 1 or numero_usuario > 5:
        print("Número fuera de rango. Debe estar entre 1 y 5.")
    elif numero_usuario == numero:
        print("¡Número acertado!")
        break
    else:
        intentos-= 1
        if intentos > 0:
            print(f"Número no acertado, te quedan {intentos} intentos.")
        else:
            print("Te quedaste sin intentos. El número era", numero)

print("Fin del programa")