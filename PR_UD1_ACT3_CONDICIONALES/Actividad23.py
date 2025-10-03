# Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un 
# notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota 
# introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota=float(input("Introduce la nota que has sacado: "))

if 8.5 <= nota <= 10:
    print(f"Tu nota es {nota}, excelente")
elif 7 <= nota < 8.5:
    print(f"Tu nota es {nota}, notable")
elif 6 <= nota < 7:
    print(f"Tu nota es {nota}, bien")
elif 5 <= nota < 6: 
    print(f"Tu nota es {nota}, suficiente")
elif 0 <= nota < 5:
    print(f"Tu nota es {nota}, insuficiente")
else:
    print("La nota que has introducido no está entre 0 y 10")
        

