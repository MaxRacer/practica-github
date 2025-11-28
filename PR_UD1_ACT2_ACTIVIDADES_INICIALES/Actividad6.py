#A partir del programa 5. Haz que se muestre por pantalla también la frase en el orden 
#inverso en que se han introducido las palabras
import time
word1=input("Introduzca una palabra")
word2=input("Introduzca otra palabra")
word3=input("Introduzca otra palabra")
word4=input("Introduzca otra palabra")
word5=input("Introduzca otra palabra")
print(f"{word1}, {word2}, {word3}, {word4}, {word5}")
time.sleep(1)
print(f"{word5}, {word4}, {word3}, {word2}, {word1}")