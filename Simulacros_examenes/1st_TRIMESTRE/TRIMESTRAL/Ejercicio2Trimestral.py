positivo=0
negativo=0
cantidad_100=0
for i in range(7):
    numero=int(input("Introduce un número: "))
    if numero<0:
        negativo=negativo+numero
    else:
        positivo=positivo+numero
        if numero>100:
            cantidad_100=cantidad_100+1
print(f"Suma positivo: {positivo}")
print(f"Suma negativos: {negativo}")
print(f"Mayores de 100: {cantidad_100}")
