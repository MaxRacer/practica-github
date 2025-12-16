# A partir del programa anterior, modifica el código para que al introducir la letra por teclado te 
# indique en qué posición de la palabra se encuentra la letra
palabra_secreta=input("Introduce una palabra secreta: ")
print("Tienes 10 oportunidades para adivinar la palabra")
longitud=len(palabra_secreta)
oportunidades=10
for i in range(oportunidades):
    letra=input("Introduce una letra: ")
    if letra in palabra_secreta:
        if letra in palabra_secreta:
            posicion=palabra_secreta.index(letra)+1
            print(f"La letra si existe: {letra} en la posición: {posicion}")
            oportunidades=oportunidades-1
            print(f"Te quedan: {oportunidades} oportunidades")
    else:
        print(f"La letra NO existe: {letra}")
        oportunidades=oportunidades-1
        print(f"Te quedan: {oportunidades} oportunidades")
if oportunidades==0:
    print("Te quedaste sin oportunidades")