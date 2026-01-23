# Modifica el programa anterior para que sea el usuario intente adivinar la palabra escogida al 
# azar de la lista, indicando si es correcto o no. El programa debe no finaliza hasta que no se adivine 
# la palabra
import random
lista1=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
valor_aleatorio=random.choice(lista1) 
aciertos=0
print(lista1)
while aciertos==0:
    secreta=input("Introduce la palabra secreta: ")
    if secreta==valor_aleatorio:
        print("ACERTASTE")
        aciertos=1
    else:
        print("Sigue jugando")