#A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados 
# números entre 0 y 10
num1=float(input("Introduce un número entre el 1-10"))
num2=float(input("Introduce otro número entre el 1-10"))

if num1 > 10 or num1 < 0 or num2 > 10 or num2 <0:
    print("Uno o los dos números están fuera de los límites establecidos")
else:
    if num1 > num2:
        print(f"El {num1} es el mayor y el {num2} es el menor")
    else:
        if num1 < num2:
            print(f"El {num2} es el mayor y el {num1} es el menor")
        else:
            print(f"El {num1} y el {num2} son iguales")
