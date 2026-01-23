# A partir de la lista definida en el ejercicio 81, haz que se visualice por pantalla una de las 
# palabras, pero con todas sus letras desordenadas. El usuario tendrá que recolocar y acertar la 
# palabra secreta. El usuario tendrá 3 oportunidades para adivinar la palabra.

import random 
aciertos=0
lista1=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
print(lista1)
palabra=random.choice(lista1)
letras=list(palabra)
random.shuffle(letras)
palabra_desordenada="".join(letras)
print(palabra_desordenada)
while aciertos!=1:
    intento=input("¿Cual es la palabra?: ")
    if intento==palabra:
        print("Has acertado")
        aciertos=aciertos+1
        
    else:
        print("No has acertado")
        intento=input("¿Cual es la palabra?: ")