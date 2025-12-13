# Realiza un programa que permita tirar 100 veces un dado y nos presente por pantalla el número
#de veces que se repite cada número.
veces=0
veces1=0
veces2=0
veces3=0
veces4=0
veces5=0
veces6=0
import random
while veces<=100:
    dado=random.randint(1, 6)
    if dado==1:
        veces1=veces1+1
        veces=veces+1
    if dado==2:
        veces2=veces2+1
        veces=veces+1
    if dado==3:
        veces3=veces3+1
        veces=veces+1
    if dado==4:
        veces4=veces4+1
        veces=veces+1
    if dado==5:
        veces5=veces5+1
        veces=veces+1
    if dado==6:
        veces6=veces6+1
        veces=veces+1
print(f"El número de veces que ha salido el 1 han sido: {veces1}")
print(f"El número de veces que ha salido el 2 han sido: {veces2}")
print(f"El número de veces que ha salido el 3 han sido: {veces3}")
print(f"El número de veces que ha salido el 4 han sido: {veces4}")
print(f"El número de veces que ha salido el 5 han sido: {veces5}")
print(f"El número de veces que ha salido el 6 han sido: {veces6}")
