errores=0 
contraseñas=0
numero1-5=0
# requisitos  
print("La PASSWORD:")  
print("     Debe tener una longitud entre 6 y 8 caracteres.")  
print("Debe contener como mínimo:")  
print("     2 números mayores o iguales que 1 y menor o igual que 5") 
print("     1 número mayor o igual que 6 y menor o igual que 5") 
print("     2 letras minúsculas")  
print("     1 letra mayúscula")  
print("     2 símbolos (*, _, @, &,/,#)")  

while contraseñas!=3:
    password=input("Introduce una contaseña: ")
    if len(password) < 6 or len(password) > 8:  
        print(f"Error, el password tiene una longitud de {len(password)} caracteres y no cumple los requisitos")  
    else:
        for i in range(password):
            x=int(x)
            if 1 <= x <= 5 and 1 <= x <= 5:
                1-5=

