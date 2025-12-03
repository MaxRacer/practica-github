#Realiza un programa que pida dos números por teclado y presente por pantalla qué números 
#hay pares e impares en ese rango. Utiliza for. Contempla si primer valor es superior al segundo.
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
if num1>num2:
    num1, num2=num2, num1
concatenar_par=""
concatenar_impar=""

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        concatenar_par += str(i) + "-"
    else:
        concatenar_impar += str(i) + "-"

if concatenar_par:
    concatenar_par = concatenar_par[:-1]
if concatenar_impar:
    concatenar_impar = concatenar_impar[:-1]

print(f"Los números pares son: {concatenar_par}")
print(f"Los números impares son: {concatenar_impar}")
