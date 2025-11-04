print("INSTRUCCIONES")
print("1. La longitud del password tiene que tener entre 6 y 8 caracteres")
print("2. Forzar los siguientes valores según la posición indicada:")
print("     Posición 1 Un número major o igual que 1 i menor o igual que 5")
print("     Posición 2 Una letra minúscula")
print("     Posición 3 Una letra mayúscula")
print("     Posición 4 Uno de los siguientes símbolos *, _, @")
print("     Posición 5 Una letra minúscula")
print("     Posición 6 Un número mayor o igual que 6 y menor o igual que 9")
print("     Posició 7 Uno de los siguientes símbolos &, /, #")
print("     Posició 8 Un número menor o igual que 5")
password=input("Introduce una password: ")
errores=0
#medimos longitud password
caracteres=len(password)
#primer condicional para medir ver si cumple el mínimo y el máximo de caracteres
if not len(password)>=6 or not len(password)<=8:
    print(f"ERROR, la contraseña tiene {caracteres} caracteres, lo cual no es viable.")
else:
    caracter1=(password[0])
    if caracter1.isnumeric():
        if 1<=int(caracter1) and 5>=int(caracter1):
            password_correcta=True
        else:
            print("ERROR en el caracter 1")
            errores=errores+1
    else:
        print("ERROR en el caracter 1")
        errores=errores+1
    caracter2=(password[1])

    if caracter2.isalpha():
        if caracter2.islower():
            password_correcta=True
        else:
            print("ERROR en el caracter 2")
            errores=errores+1
    else:
        print("ERROR en el caracter 2")
        errores=errores+1

    caracter3=(password[2])
    if caracter3.isalpha():
        if caracter3.isupper():
            password_correcta=True
        else:
            print("ERROR en el caracter 3")
            errores=errores+1
    else:
        print("ERROR en el caracter 3")

    caracter4=(password[3])
    if caracter4=="*" or caracter4=="_" or caracter4=="@":
        password_correcta=True
    else:
        print("ERROR en el caracter 4")
        errores=errores+1

    caracter5=(password[4])
    if caracter5.isalpha():
        if caracter5.islower():
            password_correcta=True
        else:
            print("ERROR en el caracter 5")
            errores=errores+1
    else:
        print("ERROR en el caracter 5")
        errores=errores+1

    caracter6=(password[5])
    if caracter6.isnumeric():
        if 6<=int(caracter6) and 9>=int(caracter6):
            password_correcta=True
        else:
            print("ERROR en el caracter 6")
            errores=errores+1
    else:
        print("ERROR en el caracter 6")
        errores=errores+1

    if len(password)==6 and errores==0 and password_correcta==True:
        print("El formato de password es correcto")  
    elif len(password)==6 and errores>0:
        print(f"La contraseña no es correcta. Tiene {errores} errores")

    if len(password)>=7:
        caracter7=(password[6])
        if caracter7=="&" or caracter7=="/" or caracter7=="#":
            password_correcta=True
        else:
            print("ERROR en el caracter 7")
            errores=errores+1

    if len(password)==7 and errores==0:
        print("El formato de password es correcto")
    elif len(password)==7 and errores>0:
        print(f"La contraseña no es correcta. Tiene {errores} errores")

    if len(password)==8:
        caracter8=(password[7])
        if caracter8.isnumeric():
            if int(caracter8)<=5:
                password_correcta=True
            else:
                print("ERROR en el caracter 8")
                errores=errores+1
        else:
            print("ERROR en el caracter 8")
            errores=errores+1
    if len(password)==8 and errores==0:
        print("El formato de password es correcto")
    elif len(password)==8 and errores>0:
        print(f"La contraseña no es correcta. Tiene {errores} errores")



