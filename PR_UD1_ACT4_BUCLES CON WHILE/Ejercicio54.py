# Modifica el programa anterior y haz que se repita el ciclo automáticamente hasta que el total 
# de todas las sumas sea superior a 50, será entonces cuando el programa finalice. No hará falta 
# preguntar si deseas repetir la operación. En cada operación aparece por pantalla la suma de la 
# operación y su acumulado. Para aquellos de vosotros que os fijáis en los detalles, controlar que el 
#mensaje del acumulado es singular o plural.. . Con While
sum_total=0
veces=0
while sum_total!=50 or sum_total>50:
    num1=int(input("Introduce un número:"))
    num2=int(input("Introduce otro número: "))
    suma=num1+num2
    sum_total=sum_total+suma
    veces=veces+1
    print("El resultado de la suma es", suma)
    if veces==1:
        print(f"El total acumulado es: {sum_total} y llevas {veces} operación realizada")
    else:
        print(f"El total acumulado es: {sum_total} y llevas {veces} operaciones realizadas")
print("Fin del programa")