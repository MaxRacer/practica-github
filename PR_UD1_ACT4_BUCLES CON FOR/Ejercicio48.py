# Realiza un programa que introduzcas por teclado una palabra ‘secreta’, consigue la longitud de 
# esa palabra para que sea ese el criterio que establezca el rango del bucle de manera que el usuario
# tenga x oportunidades para ver si letra introducida está en esa palabra.
palabra_secreta=input("Introduce una palabra secreta: ")
print("Tienes 10 oportunidades para adivinar la palabra")
longitud=len(palabra_secreta)
oportunidades=10
for i in range(oportunidades):
    letra=input("Introduce una letra: ")
    if letra in palabra_secreta:
        print(f"La letra si existe: {letra}")
        oportunidades=oportunidades-1
        print(f"Te quedan: {oportunidades} oportunidades")
    else:
        print(f"La letra NO existe: {letra}")
        oportunidades=oportunidades-1
        print(f"Te quedan: {oportunidades} oportunidades")
if oportunidades==0:
    print("Te quedaste sin oportunidades")