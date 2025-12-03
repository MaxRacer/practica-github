# Programa que pida continuamente números por teclado hasta que el usuario introduzca el valor 
#-99. Por pantalla debe aparecer cuál de todos los números introducidos es el mayo y cuál el menor
mayor=0
menor=0
numero=int(input("Introduce un número: "))
while numero!=-99:
    if numero>mayor:
        mayor=numero
    if numero<menor:
        menor=numero
    numero=int(input("Introduce un número: "))
print(mayor)
print(menor)