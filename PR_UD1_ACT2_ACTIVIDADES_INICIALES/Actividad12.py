# Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor
# y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.
print("A continuación introducirás los valores de un trapecio isósceles")
lado=float(input("Introduce el valor del lado"))
altura=float(input("Introduce el valor de la altura"))
basemenor=float(input("Introduce el valor de la base menor"))
basemayor=float(input("Introduce el valor de la base mayor"))
área=(basemayor+basemenor)*altura/2
perímetro=basemayor+basemenor+2*lado
print("El perímetro es:", perímetro)
print("El área es:", área)