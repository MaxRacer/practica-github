#Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.
#Falta poner los operadores lógicos
nota=float(input("Introduce la nota que has sacado: "))
if nota >= 8.5 and nota <= 10:
    print(f"Tu nota es {nota}, excelente")
elif nota >= 7 and nota < 8.5:
    print(f"Tu nota es {nota}, notable")
elif nota >= 6 and nota < 7:
    print(f"Tu nota es {nota}, bien")
elif nota >= 5 and nota < 6: 
    print(f"Tu nota es {nota}, suficiente")
elif nota >= 0 and nota < 5:
    print(f"Tu nota es {nota}, insuficiente")
else:
    print("La nota que has introducido no está entre 0 y 10")
        