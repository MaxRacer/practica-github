entrada=input()
partes=entrada.split()
a1=int(partes[0])
b1=int(partes[1])
a2=int(partes[2])
b2=int(partes[3])
if a1==a2 and b1==b2:
    resultado="="
elif a1>=a2 and b1<=b2:
    resultado="1"
elif a2>=a1 and b2<=b1:
    resultado="2"
else:
    resultado="?"
izquierda=max(a1, a2)
derecha=min(b1, b2)
if izquierda>derecha:
    intervalo="[]"
else:
    intervalo=f"[{izquierda},{derecha}]"
print(f"{resultado } , {intervalo}")
