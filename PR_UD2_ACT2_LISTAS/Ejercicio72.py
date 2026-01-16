# A partir del ejercicio anterior, se da por hecho que las vocales con o sin acento son repetidas y 
# no deben almacenarse en la lista
continuar = "s"
milista = []
while continuar == "s":
    letra = input("Introduce una letra: ")
    if letra in "áàäâ":
        letra = "a"
    elif letra in "éèëê":
        letra = "e"
    elif letra in "íìïî":
        letra = "i"
    elif letra in "óòöô":
        letra = "o"
    elif letra in "úùüû":
        letra = "u"

    if not letra.isnumeric():
        milista.append(letra)
    continuar=input("¿Deseas repetir s/n: ")

lista_sin_duplicados = sorted(list(set(milista)))
print(lista_sin_duplicados)
