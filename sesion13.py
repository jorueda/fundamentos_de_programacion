"""
Matrices o vectores bidimensionales

En Python podemos trabajar los arreglos bidimensionales como listas de listas, es decir, cada elemento de la lista es una lista.

Nota Existe una librería en Python que maneja tanto vectores como matrices llamada numpy. 
Esta librería está por fuera del alcance de este curso pero puedes investigarla.

Veamos un ejemplo:
"""
def ejemplo1():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    print(a)
    print(a[1][2]) # Imprimir el 8

#ejemplo1()

#O podemos recorrer todos los elementos e imprimir como una matriz
def ejemplo2():
    a = [[1, 2, 3, 4, 5],
     [6, 7, 8, 9, 0]]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' | ')
        print()

#ejemplo2()

#Actividad 1
def actividad1():
    from random import randint
    from os import system

    def generar_vector(filas, columnas):
        longitud_total = filas * columnas
        vector = []
        aleatorio = randint(10, 99)
        vector.append(aleatorio)
        for contador in range(longitud_total):
            while vector.count(aleatorio) > 0:
                aleatorio = randint(10, 99)
            vector.append(aleatorio)

        return vector

    def imprimir_matriz(vector, filas, columnas):
        matriz = []
        contador = 0
        for fila in range(filas):
            temporal = []
            for columna in range(columnas):
                temporal.append(vector[contador])
                contador += 1
            matriz.append(temporal)
            print(temporal)

        return matriz


    def max_min(matriz):
        max = 0
        min = 101
        posicion_max = []
        posicion_min = []

        for fila in range(len(matriz)):
            for columna in range(len(matriz)):
                if matriz[fila][columna] > max:
                    max = matriz[fila][columna]
                    posicion_max = [fila, columna]
                if matriz[fila][columna] < min:
                    min = matriz[fila][columna]
                    posicion_min = [fila, columna]
        print(f"El número máximo es {max} ubicado en la fila {posicion_max[0]} columna {posicion_max[1]}.")
        print(f"El número mínimo es {min} ubicado en la fila {posicion_min[0]} columna {posicion_min[1]}.")

    cantidad_filas = int(input("Ingrese el número de filas deseadas para la matriz máximo 9: "))
    cantidad_columnas = int(input("Ingrese el número de columnas deseadas para la matriz máximo 9: "))
    vector_generado = generar_vector(cantidad_filas, cantidad_columnas)
    matriz_generada = imprimir_matriz(vector_generado, cantidad_filas, cantidad_columnas)
    max_min(matriz_generada)

#
#Vamos a escribir una funcion que llene una matriz de 5 filas y 10 columnas con números enteros entre 1 y 100
#aleatorios, imprima los valores máximo y mínimo y sus posiciones dentro de la matriz.

#actividad1()

#Actividad 2
def actividad2(): 

    def generar_matriz():
        from random import sample
        filas = int(input("Ingrese el número de filas: "))
        columnas = int(input("Ingrese el número de columnas: "))
        matriz = []
        bolsa = sample(range(10, 50), 40)
        print(bolsa)
        contador = 0
        for fila in range(filas):
            temporal = []
            for columna in range(columnas):
                temporal.append(bolsa[contador])
                contador += 1
            matriz.append(temporal)

        return matriz

    def escalar(matriz, escalar):
        matriz_final = []
        for fila in matriz:
            temporal = []
            for columna in fila:
                temporal.append(columna * escalar)
            matriz_final.append(temporal)
        return matriz_final

    matriz_inicial = generar_matriz()
    print(matriz_inicial)
    resultado = escalar(matriz_inicial, 21)
    print(resultado)
    
#
#El producto escalar de un número real, x , y una matriz A es la matriz xA. 
#Cada elemento de la matriz xA es x veces su elemento correspondiente en A.
#
#Diseñemos una funcion escalar(matriz, escalar) que dada matriz[n][m] y un escalar, 
#imprima el producto escalar de la matriz.

actividad2()