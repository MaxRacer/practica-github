#Diseña un programa que al introducir un número, realice su tabla de multiplicar del 1 al 10. 
#Utiliza únicamente el while
numero=int(input("Introduce un número: "))
i=1
while i<=10:
    producto=numero*i
    i=i+1
    print(producto)