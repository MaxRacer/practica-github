listasnumeros=[]
listasnonumeros=[]
listatodo=[]

frase=input("Introduce valores separados por un guión: ")
listatodo=frase.split("-")
print(listatodo)

for x in range(len(listatodo)):
    if listatodo[x].isnumeric():
        listasnumeros.append(int(listatodo[x]))
    else:
        listasnonumeros.append(listatodo[x])
print(listasnumeros)
print(listasnonumeros)
print(sum(listasnumeros))