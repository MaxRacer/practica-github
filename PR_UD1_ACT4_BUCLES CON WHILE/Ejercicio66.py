import random
import time

veces1=0
veces2=0
veces3=0
veces4=0
veces5=0
veces6=0

inicio=time.time()
while time.time()-inicio < 3:
    dado=random.randint(1, 6)
    if dado == 1:
        veces1+=1
    if dado == 2:
        veces2+= 1
    if dado == 3:
        veces3+=1
    if dado == 4:
        veces4+=1
    if dado == 5:
        veces5+=1
    if dado == 6:
        veces6+=1
tiempo_total = time.time() - inicio
print("RESUMEN:")
print(f"Tiempo: {tiempo_total}")
print(f"El número de veces que ha salido el 1 ha sido: {veces1}")
print(f"El número de veces que ha salido el 2 ha sido: {veces2}")
print(f"El número de veces que ha salido el 3 ha sido: {veces3}")
print(f"El número de veces que ha salido el 4 ha sido: {veces4}")
print(f"El número de veces que ha salido el 5 ha sido: {veces5}")
print(f"El número de veces que ha salido el 6 ha sido: {veces6}")
