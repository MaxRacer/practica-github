import random
Lista_palabrasecreta=["Alonso"]
Lista_partida=[]
Lista_ahorcado=[]
lista_errores = ["A", "H", "O", "R", "C", "A", "D", "O"]
palabra=random.choice(Lista_palabrasecreta)
for i in range(0, len(palabra)):
    Lista_partida.append("_")
print(*Lista_partida)
print("")
while "_" in Lista_partida:
    letra=input("Introduce una letra: ").upper()
    if letra in palabra:
        for x in range(len(palabra)):
            if palabra[x]==letra:
                Lista_partida[x]=letra
                print(*Lista_partida)