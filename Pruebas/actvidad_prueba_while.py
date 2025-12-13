import random
intentos = 3
numero = random.randint(1, 20)

while intentos>0:
    numero_usuario = int(input("Introduce un número entre el 1-20: "))
    if numero_usuario == numero:
        print("Acertaste!")
        break
    elif numero_usuario > numero:
        print("Es menor")
    else:
        print("Es mayor")
    intentos=intentos-1
    print("Te quedan", intentos, "intentos")
if intentos==0:
    print("Se acabaron los intentos. El número era", numero)
