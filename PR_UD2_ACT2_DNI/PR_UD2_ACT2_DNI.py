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

        if resto < 0 or resto > 22:
            print("Error: resto no válido")
            lista_intentos.append(2)
            dnis_incorrectos.append(dni)
        else:
            letra=letras[resto]
            nif=dni + "-" + letra
            print("NIF:", nif)
            lista_intentos.append(3)
            dnis_correctos.append(nif)

    seguir = input("¿Continuar? (s/n): ")


print("MENÚ:")
print("1. Listar DNI correctos ordenados de menor a mayor")
print("2. Listar DNI incorrectos ordenados de menor a mayor")
print("3. Número total de errores")
print("4. Número total de DNIs correctos")
print("5. Porcentajes")

opcion=input("Elige una opción: ")
if opcion=="1":
    print("DNI correctos:")
    for dni in sorted(dnis_correctos):
        print(dni)
elif opcion=="2":
    print("DNI incorrectos:")
    for dni in sorted(dnis_incorrectos):
        print(dni)
elif opcion=="3":
    errores=lista_intentos.count(0) + lista_intentos.count(1) + lista_intentos.count(2)
    print("Número total de errores:", errores)
elif opcion=="4":
    print("Número total de DNIs correctos:", lista_intentos.count(3))
elif opcion=="5":
    total=len(lista_intentos)
    if total > 0:
        print("% DNIs correctos:", lista_intentos.count(3)*100 / total)
        print("% DNIs incorrectos:", (total - lista_intentos.count(3))*100 / total)
        print("% Error longitud:", lista_intentos.count(0)*100 / total)
        print("% Error no numérico:", lista_intentos.count(1)*100 / total)
        print("% Error no existente:", lista_intentos.count(2)*100 / total)
    else:
        print("No hay datos")

else:
    print("Opción no válida")