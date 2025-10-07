#Realiza un programa que, al introducir una letra por teclado, aparezca por pantalla si 
# está o no en mayúscula. Utiliza dos IF’s que establezcan True o False a la condición.
letra = input("Introduce una letra: ")

if letra.isupper():
    mayor = True
else:
    mayor = False

if not letra.isupper():
    menor = True
else:
    menor = False
print(f"¿La letra '{letra}' está en mayúscula? {mayor}")
print(f"¿La letra '{letra}' no está en mayúscula? {menor}")
elif len(letra)!= 1 or not letra.isalpha():
print(f"¿La letra '{letra}' no es una letra")
