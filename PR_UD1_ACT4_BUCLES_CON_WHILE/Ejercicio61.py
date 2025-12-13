#A partir del código anterior, haz que el programa finalice si el valor de la tabla de multiplicar es
#superior o igual a 40.
numero=int(input("Introduce un número: "))
i=1
while i<=10:
    producto=numero*i
    i=i+1
    print(producto)
    if producto>=40:
        print("Fin del programa")
        break