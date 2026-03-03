import random
import time
Lista_palabrasecreta=[
"ALONSO","VERSTAPPEN","HAMILTON","LECLERC","NORRIS",
"SAINZ","RUSSELL","PIASTRI","PEREZ","STROLL"
]

Lista_ahorcado=["A","H","O","R","C","A","D","O"]
continuar="S"
while continuar=="S" and len(Lista_palabrasecreta)>0:
    añadir=input("¿Quieres añadir una palabra secreta? (S/N): ").upper()
    if añadir=="S":
        nueva=input("Introduce la nueva palabra: ").upper()
        Lista_palabrasecreta.append(nueva)

    palabra=random.choice(Lista_palabrasecreta)
    Lista_palabrasecreta.remove(palabra)
    Lista_partida=[]
    Lista_aciertos=[]
    Lista_errores=[]
    errores=0

    for i in range(len(palabra)):
        Lista_partida.append("_")
    print("PALABRA:")
    print(*Lista_partida)

    inicio=time.time()
    while "_" in Lista_partida and errores<8:
        letra=input("Introduce una letra: ").upper()
        if letra in Lista_aciertos or letra in Lista_errores:
            print("Ya has usado esa letra")
            continue
        if letra in palabra:
            Lista_aciertos.append(letra)

            for x in range(len(palabra)):
                if palabra[x]==letra:
                    Lista_partida[x]=letra

        else:
            Lista_errores.append(letra)
            errores+=1
            print("La letra no está en la palabra")
            print(*Lista_ahorcado[:errores])

        print(f"Palabra: {Lista_partida}")
        print(f"Aciertos: {Lista_aciertos}")
        print(f"Errores: {Lista_errores}")

    fin=time.time()
    tiempo=fin-inicio

    minutos=int(tiempo//60)
    segundos=int(tiempo%60)

    if "_" not in Lista_partida:
        print("¡HAS GANADO!")
    else:
        print("HAS PERDIDO")
        print(f"La palabra era: {palabra}")
    aciertos=len(Lista_aciertos)
    print("RESUMEN PARTIDA")
    print(f"Palabra secreta: {palabra}")
    print(f"Número de aciertos:{aciertos}")
    print(f"Número de errores: {errores}")
    print(f"Tiempo: {minutos} min y {segundos} segundos")

    if len(Lista_palabrasecreta)==0:
        print("No quedan más palabras.")
        continuar="N"
    else:
        continuar=input("¿Quieres jugar otra partida? (S/N): ").upper()

print("Fin del juego")

