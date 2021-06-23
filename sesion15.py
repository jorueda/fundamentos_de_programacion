"""
Matrices o vectores bidimensionales

Vamos a utilizar esta sesión para repasar los conceptos vistos y a aprender otras funciones interesantes 
en Python.

La función string.split(), por ejemplo, toma una cadena de caracteres (string) y la pasa a una lista.
Por defecto el separador es cada espacio en blanco, pero se puede seleccionar cualquier separador. 
Veamos un ejemplo:
"""
def ejemplo1(frase):
    lista = frase.split()
    print(lista)

#ejemplo1("Esta es una prueba para pasar a una lista")

#Actividad 1

def actividad1(texto, numero):

    cadena = []
    cadena = texto.split()
    lista = []
    for palabra in cadena:
        if len(palabra) > numero:
            lista.append(palabra)

    return lista

#
#Escribe una función actividad1(x, n) que reciba una frase x y un numero entero n 
#e imprima una lista con las palabras cuya longitud sea mayor a n de entrada.

#print(actividad1("Esta es una prueba para pasar a una lista",3))

#Actividad 2

def crearMatriz(m, n):
    from random import randint

    matriz = []
    for fila in range(m):
        temporal = []
        for columna in range(n):
            temporal.append(randint(0, 9))
        matriz.append(temporal)

    return matriz

def calcularPromedio(T):
    contador = 0
    acumulado = 0
    for fila in T:
        for columna in fila:
            contador += 1
            acumulado += columna
    prom = acumulado / contador

    return prom

def actividad2(m, n):
    matriz = crearMatriz(m, n)
    print(matriz)
    promedio = calcularPromedio(matriz)
    print("El promedio es: {0:.2f}".format(promedio))
    matriz_final = []
    for fila in matriz:
        temporal = []
        for columna in fila:
            if columna >= promedio:
                temporal.append(1)
            else:
                temporal.append(0)
        matriz_final.append(temporal)   
    print(matriz_final)
     
#
#Creemos ahora una función crearMatriz(m,n) que genere una matriz de M * N con números aleatorios 
#entre 0 y 9 y la retorne.
#
#Creemos también una función calcularPromedio(T) que dada una matriz T, genere un promedio de todos 
#sus elementos y lo retorne.
#
#Finalmente una función actividad2(m,n) que llame a crearMatriz, pase esa matriz a calcularPromedio(T) 
#y que genere una matriz que tenga el valor 1 en aquellas posiciones donde el valor sea mayor o igual 
#al promedio en T y cero (0) donde el valor de la posición en T sea menor que el promedio.
#
#Imprimir ambas matrices.

actividad2(3, 3)