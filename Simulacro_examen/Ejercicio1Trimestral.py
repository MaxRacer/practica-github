inicio=int(input("Introduce el inicio: "))
final=int(input("Introduce el final: "))
incremento=int(input("Introduce el incremento: "))
concatenar=""
for i in range(inicio, final, incremento):
    if not i%4==0:
        if i%6==0:
            concatenar=concatenar+"*"+str(i)+"*"+","
        else:
            concatenar=concatenar+str(i)+","

concatenar=concatenar[:-1]
print(concatenar)