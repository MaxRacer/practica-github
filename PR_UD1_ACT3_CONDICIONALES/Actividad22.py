# Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. 
# Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.
nota=float(input("Introduce la nota que has sacado: "))
if nota<0 or nota>10:
    print("La nota que has introducido no está entre 0 y 10")
else:
    if nota<5:
        print(f"Tu nota es {nota} y has suspendido")
    else:
        print(f"Tu nota es {nota} y has aprobado")