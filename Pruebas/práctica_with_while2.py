edad=int(input("Introduce la edad: "))
while edad>99 or edad<=0:
    print("Edad incorrecta")
    edad=int(input("Vuelve a introducir la edad"))
print("Tu edad es correcta")
import time
time.sleep(3)