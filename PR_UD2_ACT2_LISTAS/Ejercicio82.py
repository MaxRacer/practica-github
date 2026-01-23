# Modifica el código del ejercicio anterior para que el programa permita repetir x partidas (hasta 
# que el usuario lo decida). Tienes que controlar una puntuación de cada partida de la siguiente 
# manera, si la palabra la aciertas a la primera son 8 puntos, si la aciertas a la segunda 7 puntos y así 
# sucesivamente.
# Una vez el usuario desea finalizar el programa tiene que sumar todas tus puntuaciones obtenidas. 
# Si el total supera la media de la puntuación posible de todas las partidas, se puede decir que la 
# suerte le acompaña, de lo contrario mejor no Se dediques a los juegos de azar . PISTA.. ¿existe 
# algún método que permita sumar el contenido de una lista?
import random
lista_palabras=["casa", "barco", "gato", "perro", "madera", "agua", "puente", "pantalón"]
puntuaciones=[]
num_partidas = int(input("¿Cuántas partidas quieres jugar? "))
partidas_totales=num_partidas
while num_partidas>0:
    palabra_secreta = random.choice(lista_palabras)
    puntos_restantes=8
    acertado=False
    print("Nueva partida. Palabras disponibles:")
    print(lista_palabras)
    while not acertado:
        intento = input("Introduce la palabra secreta: ")
        if intento == palabra_secreta:
            print("¡ACERTASTE!")
            puntuaciones.append(puntos_restantes)
            acertado = True
            num_partidas -= 1
        else:
            print("Sigue intentando...")
            puntos_restantes -= 1
            if puntos_restantes == 0:
                print("Te quedaste sin puntos. La palabra era:", palabra_secreta)
                puntuaciones.append(0)
                num_partidas -= 1
                acertado = True

puntuacion_total = sum(puntuaciones)
puntuacion_maxima = partidas_totales * 8
media = puntuacion_maxima / partidas_totales


print(f"Puntuaciones obtenidas: {puntuaciones}")
print(f"Puntuación total: {puntuacion_total}")
print(f"Puntuación media posible: {media}")

if puntuacion_total > media:
    print("La suerte te acompaña.")
else:
    print("Mejor no te dediques a los juegos de azar.")

