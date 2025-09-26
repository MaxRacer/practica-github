# Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg)
# y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25,
# debe aparecer un mensaje informando de sobrepeso.
peso=float(input("¿Cuánto pesas en KG?"))
altura=float(input("¿Cuánto mides en M?"))
IMC=peso/altura**2
IMC_redondeado=round(IMC, 2)
if IMC > 25:
    print("Si pesas", peso, "kilos y mides", altura, "m, tu IMC es:", IMC_redondeado,". Hay sobrepeso")
else:
    print("Si pesas", peso, "kilos y mides", altura, "m, tu IMC es:", IMC_redondeado)