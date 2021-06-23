# reto2
# Los valores de entrada se ingresan uno a uno

numero_lecturas = int(input())
contador = 1
acidez = 0
materia_organica = 0
acumulado_acidez = 0
acumulado_materia_organica = 0
sumamente_apto = 0
moderadamente_apto = 0
marginalmente_apto = 0
no_apto = 0

while contador <= numero_lecturas:
    acidez = float(input())
    materia_organica = float(input())
    acumulado_acidez += acidez
    acumulado_materia_organica += materia_organica
    contador += 1

    if acidez > 5.5 and acidez <= 6.5:
        calificacion_acidez = 1
    elif (acidez > 6.5 and acidez <= 7) or (acidez > 5 and acidez <= 5.5):
        calificacion_acidez = 2
    elif (acidez > 7 and acidez <= 8) or (acidez >= 4.5 and acidez <=5):
        calificacion_acidez = 3
    else:
        calificacion_acidez = 4

    if materia_organica > 5:
        calificacion_materia = 1
    elif materia_organica > 4 and materia_organica <= 5:
        calificacion_materia = 2
    elif materia_organica >= 3 and materia_organica <=4:
        calificacion_materia = 3
    else:
        calificacion_materia = 4

    if calificacion_acidez == calificacion_materia:
        resultado = calificacion_acidez
    elif calificacion_acidez < calificacion_materia:
        resultado = calificacion_materia
    else:
        resultado = calificacion_acidez

    if resultado == 1:
        sumamente_apto += 1
    elif resultado == 2:
        moderadamente_apto += 1
    elif resultado == 3:
        marginalmente_apto += 1
    else:
        no_apto += 1

print("{:.2f}".format(acumulado_acidez / numero_lecturas))
print("{:.2f}".format(acumulado_materia_organica / numero_lecturas))
print("sumamente apto", sumamente_apto)
print("moderadamente apto", moderadamente_apto)
print("marginalmente apto", marginalmente_apto)
print("no apto", no_apto)