# Reto 1 - Fundamentos de Programacion

acidez = float(input("Ingrese la Acidez del suelo (pH): "))
materia_organica =float(input("Ingrese la Materia Organica del suelo (% total): "))

if acidez >= 5.6 and acidez <= 6.5:
    calificacion_acidez = 1
elif (acidez >= 6.6 and acidez <= 7.0) or (acidez >= 5.1 and acidez <= 5.5):
    calificacion_acidez = 2
elif (acidez >= 7.1 and acidez <= 8.0) or (acidez >= 4.5 and acidez <= 5.0):
    calificacion_acidez = 3
elif acidez < 4.5 or acidez > 8:
    calificacion_acidez = 4

if materia_organica > 5:
    calificacion_materia = 1
elif materia_organica >= 4.1 and materia_organica <= 5:
    calificacion_materia = 2
elif materia_organica >= 3 and materia_organica <= 4:
    calificacion_materia = 3
elif materia_organica < 3:
    calificacion_materia = 4

if calificacion_acidez == calificacion_materia:
    resultado = calificacion_acidez
elif calificacion_acidez < calificacion_materia:
    resultado = calificacion_materia
else:
    resultado = calificacion_acidez

if resultado == 1:
    print("Sumamente apto")
elif resultado == 2:
    print("Moderadamente apto")
elif resultado == 3:
    print("Marginalmente apto")
else:
    print("No apto")
