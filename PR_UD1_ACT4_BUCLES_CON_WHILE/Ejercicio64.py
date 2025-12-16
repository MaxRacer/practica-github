# Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Será entonces cuando por pantalla aparecerán las siguientes estadísticas:
#a) total de pares
#b) total de impares
#c) total de números positivos
#d) total de números negativos
#e) total de ceros
#f) total de la suma de todos los números introducidos
pares=0
impares=0
positivos=0
negativos=0
total_ceros=0
total_suma=0
numero=int(input("Introduce un número: "))
while numero!=-99:
    if numero%2==0:
        pares=pares+1
        if numero<0:
            negativos=negativos+1
            total_suma=total_suma+numero
        else:
            positivos=positivos+1
            total_suma=total_suma+numero
    else:
        impares=impares+1
        if numero<0:
            negativos=negativos+1
            total_suma=total_suma+numero
        else:
            positivos=positivos+1
            total_suma=total_suma+numero
    if numero==0:
        total_ceros=total_ceros+1
    numero=int(input("Introduce un número: "))
print("RESUMEN")
print(f"El número de pares es: {pares}")
print(f"El número de impares es: {impares}")
print(f"El número de positivos es: {positivos}")
print(f"El número de negativos es: {negativos}")
print(f"El total de ceros es: {total_ceros}")
print(f"El TOTAL es: {total_suma}")