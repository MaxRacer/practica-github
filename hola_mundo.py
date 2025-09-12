import time
print("Hola, me gusta Python")
time.sleep(1)
var1=input("¿A ti también te gusta? S/N")
if var1=="S":
    print("A mí también")
    
    var2=input("¿Quieres aprender programación para crear tus propios programas o proyectos? S/N")
    if var2=="S":
        print("Perfecto, en internet hay un montón de tutoriales que te ayudarán a aprender por ti mismo")
    else:
        print("Siempre es bueno aprender... pero bueno si no quieres, tú te lo pierdes")
else:
    print("Que mal gusto tienes")
