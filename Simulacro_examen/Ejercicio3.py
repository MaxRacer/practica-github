import math
radio=float(input("Introduce el radio de un cilindro"))
altura= float(input("Introduce la altura de un cilindro"))
respuesta="El volumen del cilindro es: "
mayusculas_or_minusculas=input("Quieres el resultado en mayusculas (M) o en minusculas (m): ")
resultado=math.pi*radio**2*altura
resultado_redondeado=round(resultado,3)
if mayusculas_or_minusculas == "M":
    print(f"{respuesta.upper}{resultado_redondeado}")
elif mayusculas_or_minusculas == "M":
    print(f"{respuesta.lower}{resultado_redondeado}")
    
else:
    print("Error")