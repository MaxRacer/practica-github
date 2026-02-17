entrada=input()
partes=entrada.split()
euros=int(partes[0])
centimos=int(partes[1])
billetes=[500, 200, 100, 50, 20, 10, 5]
for b in billetes:
    cantidad=euros//b
    print(f"Banknotes of {b} euros: {cantidad}")
    euros=euros%b

monedas_euro=[2, 1]
for m in monedas_euro:
    cantidad=euros//m
    if m==2:
        print(f"Coins of 2 euros: {cantidad}")
    else:
        print(f"Coins of 1 euro: {cantidad}")
    euros=euros%m

monedas_centimos=[50, 20, 10, 5, 2, 1]
for m in monedas_centimos:
    cantidad=centimos//m
    if m==1:
        print(f"Coins of 1 cent: {cantidad}")
    else:
        print(f"Coins of {m} cents: {cantidad}")
    centimos=centimos%m