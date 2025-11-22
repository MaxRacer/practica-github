
# Introduce por teclado dos números y muestre por pantalla la siguiente información:
# cociente, resto y si el dividendo es par o impar.
var1=float(input("Introduce un número"))
var2=float(input("Introduce otro número"))
Cociente= var1/var2
Resto=var1%var2
cociente_redondeado=round(Cociente, 2)
print("El cociente es:", cociente_redondeado)
print("El resto es:", Resto)

if var1 % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")