# Realiza un programa que permita introducir una cantidad exacta de números, cada número se 
# irá almacenando en una lista. El programa debe finalizar presentando por pantalla los números 
# ordenados de menor a mayor.
usuario=0
lista=[]
usuario=int(input("¿Cuantos números quieres introducir?: "))
for x in range (usuario):
    num=int(input("Introduce un número: "))
    lista.append(num)
    lista.sort()
print(lista)