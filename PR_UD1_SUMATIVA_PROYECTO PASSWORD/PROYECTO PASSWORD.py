errores = 0  
# requisitos  
print("INTRODUCCIÓN")  
print("Posición 1: Un número mayor o igual 1 y menor o igual que 5")  
print("Posición 2: Una letra minúscula")  
print("Posición 3: Una letra minúscula")  
print("Posición 4: Uno de estos símbolos: *, _, @")  
print("Posición 5: Una letra minúscula")  
print("Posición 6: Un número mayor o igual 6 y menor o igual que 9")  
print("Posición 7: Uno de estos símbolos: &, /, #")  
print("Posición 8: Un número menor o igual que 5")  
# pedir al usuario la contraseña  
password = input("Introduzca una password entre 6-8 caracteres: ")  
caracteres = len(password)  
  
# ver si cumple lo mínimo y máximo de caracteres  
if len(password) < 6 or len(password) > 8:  
    print(f"Error, el password tiene una longitud de {caracteres} caracteres y no cumple los requisitos")  
else:  
    # posición 0  
    posicion0 = password[0]
    if posicion0.isnumeric():
        if 1 <= int(posicion0) <= 5:
            password_correcta=True
        else:
            print("Error en el carácter 1")
            errores += 1        
    else:  
        print("Error en el carácter 1")  
        errores += 1 
    # posición 1
    posicion1=password[1]
    if posicion1.isalpha():
        password_correcta=True
        if posicion1.islower():
            password_correcta=True
        else:
            print("Error en el carácter 2")
            errores += 1   
    else:
        print("Error en el carácter 2")
        errores += 1   
    # posición 2
    posicion2=password[2]
    if posicion2.isalpha():
        password_correcta=True
        if posicion2.isupper():
            password_correcta=True
        else:
            print("Error en el carácter 3")
            errores += 1   
    else:
        print("Error en el carácter 3")
        errores += 1   
    #posición 3
    if password[3] == "*" or password[3] == "_" or password[3] == "@":
        password_correcta=True
    else:
        print("Error en el carácter 4")
        errores += 1  
    # posición 4
    posicion4=password[4]
    if posicion4.isalpha():
        password_correcta=True
        if posicion4.islower():
            password_correcta=True
        else:
            print("Error en el carácter 5")
            errores += 1   
    else:
        print("Error en el carácter 5")
        errores += 1   
    # posición 5
    posicion5 = password[5]
    if posicion5.isnumeric:
        if 6 <= int(posicion5) <= 9:
            password_correcta=True
        else:
            print("Error en el carácter 6")
            errores += 1        
    else:  
        print("Error en el carácter 6")  
        errores += 1 
    # Posición 6
    if len(password) >= 7:  
        if password[6] == "&" or password[6] == "/" or password[6] == "#":  
            password_correcta=True  
        else:  
            print("Error en el carácter 7")  
            errores += 1   
    # Posición 7
    if len(password) == 7: 
        if password[7].isnumeric():  
            if int(password[7]) <= 5:  
                password_correcta=True 
            else:
                print("Error en el carácter 8")  
                errores += 1       
        else:  
            print("Error en el carácter 8")  
            errores += 1    
    if errores==0 and password_correcta==True:
        print("El formato de la PASSWORD es correcta")





