# Utilizando listas, crea un programa que te permita determinar si un número es decimal o no.
caracteres_decimales=['.']
seguir="s"
while seguir=="s":
    numero=input("Introduce un número: ")
    es_decimal=False

    for c in caracteres_decimales:
        if c in numero:
            es_decimal=True

    if es_decimal==True:
        print("El número es decimal.")
    else:
        print("El número NO es decimal.")

    seguir = input("¿Deseas introducir otro valor? s/n: ")
    
