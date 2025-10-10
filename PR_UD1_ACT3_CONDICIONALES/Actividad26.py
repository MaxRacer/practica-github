#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
# está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")
if letra.isupper():
    mayor = True
    print(f"¿La letra '{letra}' está en mayúscula? {mayor}")
elif letra.isnumeric():
    print(f"¿La letra '{letra}' no es una letra")
else:
    letra.islower()
    mayor = False
    print(f"¿La letra '{letra}' está en mayúscula? {mayor}")



