print("MENÚ")
print(" 1. Bocadillo de calamares- 9 €")
print(" 2. Bocadillo de chistorra - 4.5 €")
print(" 3. Bikini de jamón - 2.5 €")
print("ACOMPAÑAMIENTO")
print(" 1. Patatas finas - 1.5 €")
print(" 3. Patatas gruesas - 1.75 €")
print(" 3. Patatas rústicas - 2 €")
print("BEBIDAS")
print(" 1. Coca cola - 2 €")
print(" 2. Acuarius - 1.5 €")
print(" 3. Agua - 1 €")
precio_menu=0
precio_acomp=0
precio_bebida=0
precio_total=0
menu="s"
while menu=="s":
    menu=int(input)("¿Qué menú quieres (1,2,3)?")
    acompañamiento=int(input("¿Qué acompañamiento deseas (1,2,3)?"))
    bebida=int(input("¿Qué bebida deseas (1,2,3)?"))
    if menu==1:
        precio_menu=9
    if menu==2:
        precio_menu=4.5
    if menu==3:
        precio_menu=2.5

    if acompañamiento==1:
        precio_acomp=1.5
    if acompañamiento==2:
        precio_acomp=1.75
    if acompañamiento==3:
        precio_acomp=2

    if bebida==1:
        precio_bebida=2
    if bebida==2:
        precio_bebida=1.5
    if bebida==3:
        precio_bebida=1
    precio_total=precio_acomp+precio_bebida+precio_menu
    if precio_total>=20 and precio_total<=30:


