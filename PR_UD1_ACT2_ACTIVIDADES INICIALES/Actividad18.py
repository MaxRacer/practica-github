#Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan
# importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores
# de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por
# teclado el número de menores y el número de adultos que asisten al cine.
import time
print("¡Bienvenidos a Cines Paradiso!")
time.sleep(1)
var1=int(input("¿Cuántos adultos asitirán al cine?"))
var2=int(input("¿Cuántos menores asitirán al cine?"))
precio1=var1*12
precio2=var2*12
total_precio1 = precio1 - (precio1 * 10 / 100)
total_precio2 = precio2 - (precio2 * 50 / 100)
print("El precio total del cine para", var1, "mayor/es es:", total_precio1)
print("El precio total del cine para", var2, "menor/es es:", total_precio2)