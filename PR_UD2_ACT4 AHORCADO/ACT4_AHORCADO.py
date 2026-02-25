import random
Lista_palabrasecreta=["Alonso"]
Lista_partida=[]
Lista_ahorcado=["A", "H", "O", "R", "C", "A", "D", "O"]
palabra=random.choice(Lista_palabrasecreta).upper()
for i in range(len(palabra)):
    Lista_partida.append("_")
print(*Lista_partida)
print("")

while "_" in Lista_partida:
        letra=input("Introduce una letra: ").upper()
        if letra in palabra:
            for x in range(len(palabra)):
                if palabra[x] == letra:
                    Lista_partida[x] = letra
            print(*Lista_partida)
