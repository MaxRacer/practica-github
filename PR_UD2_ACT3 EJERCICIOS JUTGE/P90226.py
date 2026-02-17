palabra=input()
partes=palabra.split()
a=partes[0]
b=partes[1]
if a<b:
    print(a, "<", b)
elif a>b:
    print(a, ">", b)
else:
    print(a, "=", b)