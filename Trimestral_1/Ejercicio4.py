#inicializamos con un valor inicial la variable var_total
var_total=50
#comenzamos un bucle infinito
while True:
    #preguntamos un valor
    numero=int(input("Introduce un valor: "))
    if numero==0:
        print("Fin del programa")
        break       #primero comprobamos si ha introducido 0 por teclado, si es así sale del bucle
    #comprobamos si es par
    if numero%2==0:
        #si es par, sumamos ese valor a la variable var_total
        var_total=var_total+numero
        print(var_total)
    #si no ha cumplido la condición anterior, quiere decir que es impar
    else:
        #al ser impar, restamos ese valor a la variable var_total
        var_total=var_total-numero
        print(var_total)
    if var_total>60:        #miramos si sobrepasa el límite
        print("Fin del programa")      #si lo hace, ponemos un mensaje por pantalla de que ha finalizado y salimos del bucle
        break