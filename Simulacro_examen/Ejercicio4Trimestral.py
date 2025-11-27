valor=100
while True:
    numero=int(input("Introduce un número: "))
    if numero<0:
        break
    else:
        if numero%2==0:
            valor=valor/2
        else:
            valor=valor+numero
        if numero%3==0:
            valor=valor-5
        print(f"Valor actual: {valor}")



        if valor<50:
            break
        if valor>150:
            break