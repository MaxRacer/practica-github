print("REQUISITOS DE LA PASSWORD")
print("- Longitud entre 6 y 8 caracteres")
print("- Debe contener como mínimo:")
print("     2 números entre 1 y 5")
print("     2 letras minúsculas")
print("     1 letra mayúscula")
print("     2 símbolos (*, _, @, &, /, #)")
print("     1 número entre 6 y 9")

passwords_correctas = 0
passwords_incorrectas = 0
simbolos_validos = "*_@&/#"

for intento in range(1, 4):
    print(f"PASSWORD {intento}")
    password=input("Introduce una password: ")

    # Comprobación de longitud
    if len(password) < 6 or len(password) > 8:
        print("Password incorrecta: longitud no válida")
        passwords_incorrectas += 1
        continue

    # Contadores
    numeros_1_5 = 0
    numeros_6_9 = 0
    letras_minus = 0
    letras_mayus = 0
    simbolos = 0

    # Recorremos el password
    for caracter in password:
        if caracter.isnumeric():
            if 1 <= int(caracter) <= 5:
                numeros_1_5 += 1
            elif 6 <= int(caracter) <= 9:
                numeros_6_9 += 1

        elif caracter.isalpha():
            if caracter.islower():
                letras_minus += 1
            elif caracter.isupper():
                letras_mayus += 1

        elif caracter in simbolos_validos:
            simbolos += 1

    # Comprobación final
    if (numeros_1_5 >= 2 and
        letras_minus >= 2 and
        letras_mayus >= 1 and
        simbolos >= 2 and
        numeros_6_9 >= 1):

        print("Password CORRECTA")
        passwords_correctas += 1
    else:
        print("Password INCORRECTA")
        passwords_incorrectas += 1

# Resultados finales
print("RESULTADO FINAL")
print("Passwords correctas:", passwords_correctas)
print("Passwords incorrectas:", passwords_incorrectas)


