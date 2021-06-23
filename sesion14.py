"""
Matrices o vectores bidimensionales

Vamos a continuar con el trabajo de matrices usando lista de listas. 
Como vimos en la sesión anterior, las operaciones de este tipo de matrices se pueden realizar con ciclos anidados.
"""

#Actividad 1

def actividad1(matriz):

    columnas = len(matriz)
    for fila in matriz:
        if columnas != len(fila):
            print("La matriz no es cuadrada.")
            break
    else:
        contador = 0
        for fila in matriz:
            print(fila[contador])
            contador += 1
            

#Escribe una función actividad1(x) que imprima la diagonal principal de una matriz x. 
#Asegúrate de validar si la matriz es cuadrada, sino devuelve un mensaje, "La matriz no es cuadrada"

#actividad1([[8, 1, 3], [2, 7, 2] ,[3, 3, 4]])


#Actividad 2

def actividad2():
    
    filas = int(input("Ingrese el número de filas: "))

    matriz = []
    columna = []
    for fila in range(filas):
        ingreso = input("Ingrese la fila de datos: ").split(",")
        matriz.append(ingreso)
        columna.append(ingreso[0])

    print(*matriz[0])
    print(*columna)
    print(*matriz[1][1])
    

#Creemos ahora una función actividad2() que reciba los elementos de una matriz 3x3 e imprima:
#
#   - La primera fila
#   - La primera columna
#   - Accede al elemento en la fila 1, columna 1.
#
#Los valores son ingresados por filas [0][1], [0][2], [0][3], [1][0], etc


actividad2()