# Utiliza el método sqrt de la librería math para calcular la raíz cuadrada de un número. El
# resultado de la raíz cuadrada divídelo entre 2 de manera que se obtenga siempre un
# resultado entero. Haz que se muestre por pantalla los dos resultados de todo el proceso
# (raíz y división
import math
var1=int(input("Introduce un número"))
raiz=math.sqrt(var1)
resultado=raiz//2
print("La raíz cuadrada de", var1, "es:", raiz)
print("La resultado de la división es", resultado)