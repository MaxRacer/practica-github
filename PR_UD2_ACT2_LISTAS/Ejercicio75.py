# Crea una lista con el siguiente nombre lista1 y su contenido: a,b,D,x,r,X,3,h,w,2,i. Presenta por 
# pantalla los siguientes resultados:
# a. Cantidad total de valores
# b. Cantidad de números
# c. Cantidad de letras
# d. Cantidad de mayúsculas
# e. Suma de los valores numéricos
lista1=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
lista_num=[]
for caracter in lista1:
    longitud=len(lista1)
    if caracter.isnumeric():
        lista_num.append(caracter)
print(longitud)
print(lista_num)