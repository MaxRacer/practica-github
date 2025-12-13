# Realiza un programa que sume dos números enteros por teclado y presente el resultado por 
# pantalla. El programa preguntará si deseas o no repetir la operación. Con While
repeat="s"
while repeat!="n":
    num1=int(input("Introduce un número:"))
    num2=int(input("Introduce otro número: "))
    suma=num1+num2
    print("El resultado de la suma es", suma)
    repeat=input("Deseas repetir la operación s/n: ")
print("Programa finalizado")