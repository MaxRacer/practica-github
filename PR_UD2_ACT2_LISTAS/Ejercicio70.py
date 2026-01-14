# Crea un programa que permita introducir x palabras en una lista llamada lista1. Una vez 
# introducidas, crea una nueva lista, llamada lista2, exactamente igual a lista1. Se deben mostrar por 
# pantalla el contenidos de lista1 en orden ascendente y lista2 en orden descendente. Respeta el 
# formato de entrada y salida tal y como se muestra en el testeo.
lista1=[]
lista2=[]
cantidad_palabras=int(input("Introduce la cantidad de palabras: "))
for x in range (cantidad_palabras):
    palabra=input("Introduce una palabra: ")
    lista1.append(palabra)
lista1.sort()
lista2 = lista1.copy()
lista2.reverse()
print(f"lista 1 contiene: {lista1}")
print(f"lista 2 contiene: {lista2}")