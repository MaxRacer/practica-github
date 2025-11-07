password="a1e4jk"
total=0
for i in password:
    if i.isnumeric():
        total=total+int(i)   
print(f"{total}")
vocales="aeiouáéíóúAEIOUÁÉÍÓÚ"
contador=0
for letra in password:
    if letra in vocales:
        contador=contador+1
print(f"El total de vocales es {contador}")
