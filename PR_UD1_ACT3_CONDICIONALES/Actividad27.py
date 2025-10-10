# Mejora el programa anterior para controlar que el valor introducido es una letra y en 
# caso de introducir un número, aparezca un aviso por pantalla
letra = input("Introduce una letra: ")
if letra.isupper():
    mayor = True
    print(f"¿La letra '{letra}' está en mayúscula? {mayor}")
elif letra.isnumeric():
    print(f"El valor introducido '{letra}' es una número")
elif letra is not letra.isupper or letra.islower() or letra.isnumeric():
    print("La letra es mayúscula ¿?")
else:
    letra.islower()
    mayor = False
    print(f"¿La letra '{letra}' está en mayúscula? {mayor}")
