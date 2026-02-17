entrada=input()
partes=entrada.split()
a1=int(partes[0])
b1=int(partes[1])
a2=int(partes[2])
b2=int(partes[3])
inicio=max(a1, a2)
fin=min(b1, b2)
if inicio > fin:
    print("[]")
else:
    print(f"[{inicio},{fin}]")