# Haz un programa que permita al usuario introducir letras en una lista (cantidad indefinida), en 
# esta lista no deben almacenarse las letras que se han introducido repetidas.
continuar="s"
milista=[]
while continuar=="s":
    letra=input("Introduce una letra: ")
    if letra.isnumeric():
        letra=input("Introduce una letra: ")
    else:
        milista.append(letra)
        continuar=input("¿Deseas repetir s/n: ")
lista_sin_duplicados = list(set(milista))
lista_sin_duplicados.sort()
print(lista_sin_duplicados)