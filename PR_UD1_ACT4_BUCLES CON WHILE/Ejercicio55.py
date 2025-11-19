# Última vez que reutilizamos el mismo código.. lo prometo . A partir del programa anterior 
# haz que sea todo exactamente igual pero teniendo en cuenta que el programa se repita siempre y 
# cuando la suma acumulada sea superior a 50 o la suma acumulada sea par. Con While
sum_total=0
veces=0
while sum_total!=50 or sum_total>50 or sum_total%2==0:
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