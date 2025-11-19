#A partir del código anterior, haz que aparezca al finalizar el programa por pantalla el total las 
# sumas y el número de repeticiones. Con While
repeat="s"
veces=0
sum_total=0
while repeat!="n":
    num1=int(input("Introduce un número:"))
    num2=int(input("Introduce otro número: "))
    suma=num1+num2
    print("El resultado de la suma es", suma)
    veces=veces+1
    sum_total=sum_total+suma
    repeat=input("Deseas repetir la operación s/n: ")
print("Resumen:")
print(f"La suma total es: {sum_total} y el número de repeticiones es: {veces}")
