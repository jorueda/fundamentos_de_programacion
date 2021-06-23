def es_cuadrada(matriz):
    cuadrada = True
    for fila in matriz:
        if len(fila) != len(matriz):
            cuadrada = False
            break

    return cuadrada

def cuadro_magico(matriz):

    lista = []
    filas = len(matriz)
    diagonal_1 = 0
    diagonal_2 = 0
    for fila in range(filas):
        columnas = len(matriz[fila])
        suma_filas = 0
        suma_columnas = 0
        diagonal_1 += matriz[fila][fila]
        diagonal_2 += matriz[fila][filas - fila - 1]
        for columna in range(columnas):
            suma_filas += matriz[fila][columna]
            suma_columnas += matriz[columna][fila]

        lista.append(suma_filas)
        lista.append(suma_columnas)
    lista.append(diagonal_1)
    lista.append(diagonal_2)

    print(lista)
    valor = lista[0]
    if lista.count(valor) == len(lista):
        print("El cuadro es mágico.")
    else:
        print("El cuadro no es mágico.")


entrada = [8, 1, 6], [3, 5, 7], [4, 9, 2]
if es_cuadrada(entrada) == True:
    cuadro_magico(entrada)
else:
    print("La matriz no es cuadrada.")