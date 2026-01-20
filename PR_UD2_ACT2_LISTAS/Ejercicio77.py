# A partir de la lista definida en el ejercicio 75, haz que el programa pregunte qué valor se desea 
# eliminar de la lista, siendo únicamente los números los valores permitidos para suprimir
lista1=["a", "b", "D", "x", "r", "X", "3", "h", "w", "2", "i"]
seguir="s"
print(lista1)
while seguir == "s":
    out = input("¿Qué valor quieres eliminar de la lista?: ")
    if out.isalpha():
        print("No es un número, vuelve a intentar")
    elif out in lista1:
        lista1.remove(out)
        print(lista1)
        seguir = input("¿Deseas introducir otro valor? s/n: ")
    else:
        print("Ese valor no está en la lista")
print(lista1)

    