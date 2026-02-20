import random
Lista_palabrasecreta=["alonso"]
Lista_partida=[]
Lista_ahorcado=[]
palabra=random.choice(Lista_palabrasecreta)
for i in range(0, len(palabra)):
    Lista_partida.append("_")
print(*Lista_partida)

print("")