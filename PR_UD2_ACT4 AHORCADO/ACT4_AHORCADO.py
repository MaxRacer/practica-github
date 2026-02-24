import random
Lista_palabrasecreta=["Alonso", "Hamilton", "Vertappen", "Carlos", "colapinto", "perez", "bottas", "albon","hadjar", "russel"]
Lista_partida=[]
Lista_ahorcado=[]
lista_ahorcado = ["A", "H", "O", "R", "C", "A", "D", "O"]
palabra=random.choice(Lista_palabrasecreta)
for i in range(0, len(palabra)):
    Lista_partida.append("_")
print(*Lista_partida)
print("")
