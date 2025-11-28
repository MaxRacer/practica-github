inicio=int(input("Introduce el inicio: "))  #pedimos un número de inicio
final=int(input("Introduce el final: "))    #pedimos un número final
incremento=int(input("Introduce el incremento: "))  #pedimos un número de incremento
concatenar=""   #inicializamos la variable concatenar, para despues mostrar un mensaje todo seguido
for i in range(inicio, final, incremento):  #utilizamos un for para que compruebe todos los caracteres y yaya sumando a la variable concatenar
    concatenar=concatenar+str(i)+","    #utilizamos un string porque sino no iría el código
concatenar=concatenar[:-1]  #eliminamos el último carácter
print(concatenar)   #ponemos por pantalla el mensaje final