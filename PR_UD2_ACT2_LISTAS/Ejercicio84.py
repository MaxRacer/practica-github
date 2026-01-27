# Te piden realizar un programa en que gestionen la media y la mediana de varias de tres 
# asignaturas de legua: catalán, inglés y castellano. Una vez introducidos varios registros el 
# programa debe mostrar la media y mediana los todos los alumnos introducidos
continuar = "s"
notas_cast = []
notas_cat = []
notas_ing = []
while continuar == "s":
    estudiante=input("Nombre del estudiante: ")
    caste=int(input("Nota Castellano: "))
    cata=int(input("Nota Catalán: "))
    ingles=int(input("Nota Inglés: "))
    notas_cast.append(caste)
    notas_cat.append(cata)
    notas_ing.append(ingles)
    continuar = input("¿Quieres continuar? (s/n): ")
