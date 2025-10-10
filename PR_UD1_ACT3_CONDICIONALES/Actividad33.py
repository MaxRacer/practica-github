#Programa un código que permita contar el número de vocales de la siguiente frase: No 
#hay mal que dure cien años
frase="No hay mal que dure cien años"
frase_minuscula=frase.lower()
vocales_1="a"
vocales_2="e"
vocales_3="i"
vocales_4="o"
vocales_5="u"
contador_a=0
contador_e=0
contador_i=0
contador_o=0
contador_u=0
for letra in frase:
    if letra in vocales_1:
        contador_a=contador_a+1
    elif letra in vocales_2:
        contador_e=contador_e+1
    elif letra in vocales_3:
        contador_i=contador_i+1
    elif letra in vocales_4:
        contador_o=contador_u+1
    elif letra in vocales_5:
        contador_u=contador_u+1
print(f"El número de a es {contador_a} el número de e es {contador_e} el número de i es {contador_i} el número de o es {contador_o} y el número de u es {contador_u}")