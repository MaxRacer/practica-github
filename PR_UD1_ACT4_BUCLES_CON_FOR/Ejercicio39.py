# Programa que pida n números y que, tras introducir el último número, debe aparecer por 
# pantalla el número total de positivos, negativos y número de 0
veces = int(input("¿Cuántos números quieres introducir?: "))
numero_0=0
numero_positivos=0
numeros_negativos=0
for i in range(veces):
    numero=int(input("Introduce un número: "))
    if numero<0:
        numeros_negativos=numeros_negativos+1
    elif numero==0:
        numero_0=numero_0+1
    else:
        numero_positivos=numero_positivos+1
print(f"La cantidad de números positivos es: {numero_positivos}")
print(f"La cantidad de números negativos es: {numeros_negativos}")
print(f"La cantidad de números ceros es: {numero_0}")
