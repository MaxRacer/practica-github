# Realiza un programa donde el usuario introduzca por teclado 2 intervalos, por pantalla se debe
# mostrar el rango de números teniendo en cuenta que se a<b la secuencia será incremental y si a>b
print("A continuación pondras dos intervalos")
intervalo1=int(input("Introduce el primer intervalo: "))
intervalo2=int(input("Introduce el segundo intervalo: "))
if intervalo1<intervalo2:
    for i in range(intervalo1, intervalo2+1):
        if i == intervalo2:
            print(i)
        else:
            print(f"{i}-", end="")
elif intervalo1>intervalo2:
    for i in range(intervalo1, intervalo2 - 1, -1):
        if i != intervalo2:
            print(i, end="-")
        else:
            print(i)
else:
    print(intervalo1)