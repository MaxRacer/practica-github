# A partir del programa anterior, establece los rangos para que el usuario no pueda introducir 
# notas inferiores a 0 y superiores a 10
veces = int(input("¿Cuántas notas quieres introducir?: "))
for i in range(veces):
    nota = float(input("Introduce la nota (0-10): "))
    if nota < 0 or nota > 10:
        print("Has introducido una nota equivocada")
    else:
        if nota >= 5:  
            print("Asignatura aprobada")  
        else:  
            print("Asignatura suspendida")