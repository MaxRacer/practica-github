#Programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes 
#forzar que el resultado de la división tenga 2 decimales?
import time
number1=float(input("Introduce un número"))
number2=float(input("Introduce otro número"))
total_suma=number1+number2
total_resta=number1-number2
total_multiplicación=number1*number2
total_división=number1/number2
división_dosdecimales=round(total_división, 2)
división_entera=number1//number2
Módulo=number1%number2
Exponente=number1**number2
print("La suma de operador1 y operador2 es", total_suma)
time.sleep(1)
print("La resta de operador1 y operador2 es", total_resta)
time.sleep(1)
print("La multiplicación de operador1 y operador2 es", total_multiplicación)
time.sleep(1)
print("La división de operador1 y operador2 es", división_dosdecimales)
time.sleep(1)
print("La división entera de operador1 y operador2", división_entera)
time.sleep(1)
print("El módulo de operador1 y operador2 es", Módulo)
time.sleep(1)
print("El exponente de operador1 y operador2 es", Exponente)