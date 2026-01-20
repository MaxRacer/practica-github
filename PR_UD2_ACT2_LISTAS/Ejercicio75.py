# Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
# pantalla los siguientes resultados:
# a. Cantidad total de valores
# b. Cantidad de números
# c. Cantidad de letras
# d. Cantidad de mayúsculas
# e. Suma de los valores numéricos
lista1=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
numeros=0
letras=0
mayus=0
suma=0
for caracter in lista1:
    longitud=len(lista1)
    if caracter.isnumeric():
        numeros=numeros+1
        suma=int(caracter)+suma
    if caracter.isalpha():
        letras=letras+1
        if caracter.isupper():
            mayus=mayus+1
print(f"Cantidad total de valores: {longitud}")
print(f"Cantidad números: {numeros}")
print(f"Cantidad letras: {letras}")
print(f"Cantidad de mayúsculas: {mayus}")
print(f"Suma total: {suma}")