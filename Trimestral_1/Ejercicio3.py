suma=0  #inicializamso la variable suma
cifras=int(input("Introduce el número de cifras: "))    #preguntamamos el número de cifras
numero=int(input("Introduce un número de la misma longitud: "))     #pedimos al usuarioo que introduzca un número de la misma lonitud del valor que ha introducido anteriormente
numerostr=str(numero)   #transformamos a string para que pueda recorrer todo el número
longitud=len(numerostr)     #calculamos la longitud del string
if longitud==cifras:    #comprobamos si coincide la longutd con el número de cifras que ha introducido al principio
    for i in numerostr: #miramos cada carácter
        digito=int(i)   #para hacer la suma, tenemos que pasarlo a número
        suma=suma+digito    #realizamos la operación
else:
    print("Error, no coincide el número de cifras")     #devolvemos un mensaje porque no coincide la longitud con el número de cifras
print(f"Resultado: {suma}")     #ponemos por pantalla el resultado de la suma
