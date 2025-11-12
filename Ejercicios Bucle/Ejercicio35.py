# Programa que al introducir un número por teclado permita mostrar ese número de veces tu 
# nombre
nombre=input("Introduce tu nombre: ")
veces=int(input("¿Cuántas veces quiere que lo repita?: "))
for i in range(veces):
    print(f"{nombre}")