# A partir del programa anterior, soluciona el error que se produce en el test anterior con la 
# palabra Abrigo utilizando únicamente una instrucción.
consonates=0
vocales="aeiuoáéíóú"
vocal_palabra=""
consonante=""
palabra=input("Introduce una palabra: ")
palabra=palabra.lower()
for i in range(len(palabra)):
    if palabra[i] in vocales:
        vocal_palabra=str(vocal_palabra)+str(palabra[i])
    else:
        if palabra[i] not in vocales:
            consonante=str(consonante)+str(palabra[i])
print(f"{vocal_palabra}")
print(f"{consonante}")