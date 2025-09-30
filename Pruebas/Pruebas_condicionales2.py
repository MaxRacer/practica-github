print("Menú")
print("1. Hamburguesa")
print("2, Pizza")
print("3. Lentejas")
print("4. Bocadillo de jamóm")
opcion=int(input("¿Qué quiere para comer del menú?"))
if opcion==1:
    print("Has escogido hamburguesa")
elif opcion==2:
    print("Has escogido pizza")
elif opcion==3:
    print("Has escogido lentejas")
elif opcion==4:
    print("Has escogido bocadillo de jamón")
if opcion>4 or opcion<1:
    print("Error")