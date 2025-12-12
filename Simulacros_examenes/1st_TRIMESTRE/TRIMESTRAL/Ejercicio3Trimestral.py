cifras=int(input("Introduzca el número de cifras: "))
numero=int(input("Introduzca un número de las mismas cifras: "))
pares=0
producto=1
numerostr=str(numero)
if len (numerostr)==cifras:
    for i in numerostr:
        digito=int(i)
        producto=producto*digito
        if digito%2==0:
            pares=pares+1 
    print(f"Producto de cifras: {producto}")
    print(f"Cifras pares: {pares}")
else:
    print("Longitud incorrecta")
