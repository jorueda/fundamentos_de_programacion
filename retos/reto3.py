# reto3

lista = []
eleccion = int(input())
for entrada in range((eleccion * 2)):
    lista.append(input())

promedios = []
for contador in lista:
    lista_caracteres = contador.split()
    suma = 0
    for posicion in lista_caracteres:
        numero = float(posicion)
        suma += numero
    promedios.append(suma / len(lista_caracteres))

sumamente_apto = 0
moderadamente_apto = 0
marginalmente_apto = 0
no_apto = 0
for contador in range(0, len(promedios), 2):
    acidez = promedios[contador]
    if acidez > 5.5 and acidez <= 6.5:
        calificacion_acidez = 1
    elif (acidez > 6.5 and acidez <= 7) or (acidez > 5 and acidez <= 5.5):
        calificacion_acidez = 2
    elif (acidez > 7 and acidez <= 8) or (acidez >= 4.5 and acidez <=5):
        calificacion_acidez = 3
    else:
        calificacion_acidez = 4

    materia = promedios[contador + 1]
    if materia > 5:
        calificacion_materia = 1
    elif materia > 4 and materia <= 5:
        calificacion_materia = 2
    elif materia >= 3 and materia <=4:
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

cadena_acidez = ""
cadena_materia = ""
for contador in range(len(promedios)):
    if contador % 2 == 0:
        cadena_acidez += str("{:.2f}".format(promedios[contador])) + " "
    else:
        cadena_materia += str("{:.2f}".format(promedios[contador])) + " "

cadena_acidez = cadena_acidez.strip()
cadena_materia = cadena_materia.strip()
print(cadena_acidez)
print(cadena_materia)
print("sumamente apto", sumamente_apto)
print("moderadamente apto", moderadamente_apto)
print("marginalmente apto", marginalmente_apto)
print("no apto", no_apto)
