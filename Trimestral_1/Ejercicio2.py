entrada=0 #inicializamos las variables
negativo=0
positivo=0
while True: #inicializamos un bucle infinito
    numero=int(input("Introduce un número: "))  #pedimos al usuario que introduzca un número
    if numero<0:    #comprobamos si es negativo
        negativo=negativo+numero    #hacemos las operaciones
        entrada=entrada+1   #sumamos 1 a esta variable para que se sepa cuantos número ya ha introducido
    else:           #al no ser negativo, es positivo
        positivo=positivo+numero    #hacemos las operaciones
        entrada=entrada+1
    if entrada==6:  #despues de cada ronda comprobamos si ha introducido 6 números, y si es así salimos de bucle
        break
print(f"Suma de números positivos: {positivo}") #cuando ya ha introducido los 6 números se ponen por pantalla los resultados
print(f"Suma de números negativos: {negativo}")