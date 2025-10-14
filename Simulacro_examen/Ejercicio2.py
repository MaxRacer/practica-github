frase=input("Introduce una frase: ")
numero1=float(input("Introduce un número real: "))
numero2=float(input("Introduce otro número real: "))
numero3=float(input("Introduce otro número real: "))
frase_minusculas=frase.lower()
print(f"Frase en minusculas {frase_minusculas}")
suma=numero1+numero2+numero3
media=suma/3
media_redondeada=round(media, 2)
producto=numero1*numero2*numero3
print(f"La suma es: {suma}")
print(f"La media es: {media_redondeada}")
print(f"El producto es: {producto}")