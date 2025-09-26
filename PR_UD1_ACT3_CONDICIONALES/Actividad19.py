#  Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son 
# iguales
num1=float(input("Introduce un número"))
num2=float(input("Introduce otro número"))

if num1 > num2:
    print(f"El {num1} es el mayor y el {num2} es el menor")
else:
    if num1 < num2:
       print(f"El {num2} es el mayor y el {num1} es el menor")
    else:
        print(f"El {num1} y el {num2} son iguales")
    

 

    
