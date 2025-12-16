#  Realiza un programa que permita introducir una palabra por teclado y puedas recorrer el string
# distinguiendo vocales y las consonantes:
consonates=0
vocales="aeiuoáéíóú"
vocal_palabra=""
consonante=""
palabra=input("Introduce una palabra: ")
for i in range(len(palabra)):
    if palabra[i] in vocales:
        vocal_palabra=str(vocal_palabra)+str(palabra[i])
    else:
        if palabra[i] not in vocales:
            consonante=str(consonante)+str(palabra[i])

print(f"{vocal_palabra}")
print(f"{consonante}")
            