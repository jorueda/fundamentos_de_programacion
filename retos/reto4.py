# reto4

matriz1 = []
matriz2 = []
zonas = int(input())
for zona in range(zonas):
    matriz1.append(input())
for zona in range(zonas):
    matriz2.append(input())

def evaluar(acidez, materia):
    if acidez > 5.5 and acidez <= 6.5:
        calificacion_acidez = 1
    elif (acidez > 6.5 and acidez <= 7) or (acidez > 5 and acidez <= 5.5):
        calificacion_acidez = 2
    elif (acidez > 7 and acidez <= 8) or (acidez >= 4.5 and acidez <=5):
        calificacion_acidez = 3
    else:
        calificacion_acidez = 4

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

    return resultado

acidez_string = []
materia_string = []

# Hace split de la cadena en listas de strings
for contador in matriz1:
    acidez_string.append(contador.split())
for contador in matriz2:
    materia_string.append(contador.split())

# Convierte los strings a float
matriz_acidez = []
for fila in acidez_string:
    temporal = []
    for columna in fila:
        temporal.append(float(columna))
    matriz_acidez.append(temporal)
matriz_materia = []
for fila in materia_string:
    temporal = []
    for columna in fila:
        temporal.append(float(columna))
    matriz_materia.append(temporal)

# Obtiene el vector y la matriz de resultados
dias = 7
resultado = []
mayores_zona = []
menores_zona = []
for zona in range(zonas):
    contadores = []
    temporal = []
    for dia in range(dias):
        evaluado = evaluar(matriz_acidez[zona][dia], matriz_materia[zona][dia])
        resultado.append(evaluado)
        temporal.append(evaluado)
    mayor = 0
    menor = dias + 1
    for caracteristica in range(1, 5):
        conteo = temporal.count(caracteristica)
        if conteo > 0:
            if conteo > mayor:
                mayor = conteo
                caracteristica_mayor = caracteristica
            if conteo < menor:
                menor = conteo
                caracteristica_menor = caracteristica
    mayores_zona.append(caracteristica_mayor)
    menores_zona.append(caracteristica_menor)

print(f"{resultado.count(4)} {resultado.count(3)} {resultado.count(2)} {resultado.count(1)}")
texto = ["sumamente apto", "moderadamente apto", "marginalmente apto", "no apto"]
for zona in range(zonas):
    if zona == (zonas - 1):
        print(texto[mayores_zona[zona] - 1], end="\n")
    else:
        print(texto[mayores_zona[zona] - 1], end=",")
for zona in range(zonas):
    if zona == (zonas - 1):
        print(texto[menores_zona[zona] - 1], end="\n")
    else:
        print(texto[menores_zona[zona] - 1], end=",")
