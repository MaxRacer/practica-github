import random
Lista_palabrasecreta=["Alonso"]
Lista_partida=[]
Lista_ahorcado=["A", "H", "O", "R", "C", "A", "D", "O"]
palabra=random.choice(Lista_palabrasecreta).upper()
errores=0
for i in range(len(palabra)):
    Lista_partida.append("_")
print(*Lista_partida)
print("")
while "_" in Lista_partida and errores<8:
    letra=input("Introduce una letra: ").upper()
    if letra in palabra:
        for x in range(len(palabra)):
            if palabra[x]==letra:
                Lista_partida[x]=letra
    else:
        errores=errores+1
        print("La letra introducido no está en la palabra")
        print(*Lista_ahorcado[:errores])
    print(*Lista_partida)
if "_" not in Lista_partida:
    print("¡HAS GANADO!")
elif errores==8:
    print("HAS PERDIDO")


