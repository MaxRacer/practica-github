calculo=0
mi_lista=[1,2,3,4,5,6]
mi_listapor2=[]
maximo=max(mi_lista)
minimo=min(mi_lista)
suma=sum(mi_lista)
print(mi_lista)
print(f"Máximo {maximo}")
print(f"Mínimo {minimo}")
print(f"La suma es {suma}")

for x in range (len(mi_lista)):
    calculo=mi_lista[x]*2
    mi_listapor2.append(calculo)
print(mi_listapor2)

for x in mi_lista:
    mi_listapor2.append(x*2)
print(mi_listapor2)