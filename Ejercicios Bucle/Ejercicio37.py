# Programa que pregunte cuantas notas quiero introducir y para cada nota diga si estoy aprobado 
# o suspendido.
veces=int(input("¿Cuántas notas quieres introducir?: "))
for i in range(veces):
    nota=float(input("Introduce la nota: "))
    if nota >= 5:  
        print("Asignatura aprobada")  
    else:  
        print("Asignatura suspendida") 
