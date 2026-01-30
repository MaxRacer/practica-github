# Realiza el ejercicio del DNI que encontrarás en el Sway
letras="TRWAGMYFPDXBNJZSQVHLCKE"
lista_intentos=[]
dnis_correctos=[]
dnis_incorrectos=[]
seguir="s"

while seguir=="s":
    dni=input("Introduce DNI (8 números): ")
    if len(dni)!=8:
        print("Error: longitud incorrecta")
        lista_intentos.append(0)
        dnis_incorrectos.append(dni)
    elif not dni.isdigit():
        print("Error: no es numérico")
        lista_intentos.append(1)
        dnis_incorrectos.append(dni)
    else:
        numero=int(dni)
        resto=numero%23
        if resto<0 or resto>22:
            print("Error: resto no válido")
            lista_intentos.append(2)
            dnis_incorrectos.append(dni)
        else:
            letra=letras[resto]
            nif=dni + "-" + letra
            print("NIF:", nif)
            lista_intentos.append(3)
            dnis_correctos.append(nif)

    seguir=input("¿Continuar? (s/n): ")

print("\n--- MENÚ ---")
print("1. DNI correctos")
print("2. DNI incorrectos")
print("3. Total errores")
print("4. Total correctos")
print("5. Porcentajes")

op = int(input("Opción: "))

if op == 1:
    print(sorted(dnis_correctos))

elif op == 2:
    print(sorted(dnis_incorrectos))

elif op == 3:
    print("Errores longitud:", lista_intentos.count(0))
    print("Errores numéricos:", lista_intentos.count(1))
    print("Errores resto:", lista_intentos.count(2))

elif op == 4:
    print("Correctos:", lista_intentos.count(3))

elif op == 5:
    total = len(lista_intentos)
    print("Correctos:", lista_intentos.count(3) * 100 / total, "%")
    print("Incorrectos:", (lista_intentos.count(0)+lista_intentos.count(1)+lista_intentos.count(2)) * 100 / total, "%")




