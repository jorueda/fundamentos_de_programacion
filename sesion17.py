"""
 
LactoCaribe Ltda. usa 5 camiones para la distribución de leche a sus 10 puntos de distribución.
 
La empresa se encuentra interesada en medir la eficiencia de cada uno de los 5 camiones. Por este motivo, 
LactoCaribe te solicita crear un sistema que dada una matriz de asignación con los siguientes campos: 
 
Punto de distribución, Identificación de camión, Cantidad de litros asignados, Tiempo de despacho asignado, 
 
y una matriz de registro con los siguientes campos: 
 
Punto de distribución, Identificación de camión, Cantidad de litros despachados y Tiempo de despacho registrado 
 
calcule los siguientes indicadores de desempeño para cada camión:
 
    1.	Eficiencia en tiempos de despacho = (Tiempo de despacho registrado) / Tiempo de despacho asignado x 100
    2.	Tasa de entrega (Lt/min) = Cantidad de litros despachados / Tiempo total de despacho
    3.	Nivel de Cumplimiento de los despachos = Litros despachados / Total de litros asignados x 100
 
PROBLEMA        :   Ineficiente medición de la eficiencia de los camiones
 
META            :   calcule los siguientes indicadores de desempeño para cada camión:
 
                        1.	Eficiencia en tiempos de despacho = (Tiempo de despacho registrado) / Tiempo de despacho asignado x 100
                        2.	Tasa de entrega (Lt/min) = Cantidad de litros despachados / Tiempo total de despacho
                        3.	Nivel de Cumplimiento de los despachos = Litros despachados / Total de litros asignados x 100
 
ANÁLISIS
    Entradas    :   [desp], Registro de despachos diarios con el formato indicadores  ==> Usuario
                    [entr], Registro diario de entregas con el formato especificado   ==> Usuario
                    [ncam], Cantidad de camiones, numérico, entero, constante (5)  ==> Sistema
                    [npun], Cantidad de puntos de distribución, numérico, entero, constante (10) ==> Sistema
 
    Salidas     :   Eficiencia en tiempos de despacho por camión
                    Tasa de entrega (Lt/min) por camión
                    Nivel de Cumplimiento de los despachos por camión
 
 
    Proceso     :   a)  Leer las Entradas
                    b)  Determinar por cada camión litros entregados, entregas, incumplimientos
                    c)  Calcular indicadores por cada camión  
 
DISEÑO
 
    ESTRUCTURAS DE DATOS:
 
    Asignación (Lo que se planifica - el plan de entregas)
 
    +-------+--------+--------+---------+
    | Punto | Camión | Litros | Tiempo  |
    +-------+--------+--------+---------+
    |     8 |      2 |    100 |       2 |
    +-------+--------+--------+---------+
 
    Registrado (Lo que se ejecuta - el registro de lo que se hizo)
 
    +-------+--------+--------+---------+
    | Punto | Camión | Litros | Tiempo  |
    +-------+--------+--------+---------+
    |     8 |      2 |    100 |       3 |
    +-------+--------+--------+---------+
 
    Usando los conceptos aprendidos dentro del curso:
    1.	Diseña la solución al problema presentado
    2.	Codifica la solución
    3.	Durante la etapa de pruebas, el usuario requiere que modifiques la solución para incluir las siguientes validaciones
            i.	Que los valores de litros y tiempos asignados no sean 0 o negativos.
            ii.	Que los valores de litros y tiempos de despacho no sean 0 o negativos.
            iii.	Si una de las condiciones no se cumple, el valor incluido para ese punto de distribución y para ese camión deberá ser ignorado en el cálculo.  
"""

def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

def revisar_matriz(matriz_asigna, matriz_registr):
    for fila in range(len(matriz_asigna)):
        for columna in range(2, 4):
            if matriz_asigna[fila][columna] <= 0:
                    matriz_asigna[fila][columna] = 0
                    matriz_registr[fila][columna] = 0

    return matriz_asigna, matriz_registr

def eficiencia(matriz_asigna, matriz_registr):
    print("Camión\t| Eficiencia\t| Tasa (lt/min)\t| Nivel de cumplimiento")
    for camion in range(1, 6):
        suma_tiempoAsig = 0
        suma_tiempoReg = 0
        suma_litrosAsig = 0
        suma_litrosReg = 0
        for fila in range(len(matriz_asigna)):
            if matriz_asigna[fila][1] == camion:
                suma_tiempoAsig += matriz_asigna[fila][3]
                suma_litrosAsig += matriz_asigna[fila][2]
            if matriz_registr[fila][1] == camion:
                suma_tiempoReg += matriz_registr[fila][3]
                suma_litrosReg += matriz_registr[fila][2]

        print(f"{camion}\t|", "{:.2f}".format(suma_tiempoReg / suma_tiempoAsig * 100), "\t| {:.2f}".format(suma_litrosReg / suma_tiempoReg), "\t| {:.2f}".format(suma_litrosReg / suma_litrosAsig * 100))


def controlDespachos(matriz_asignacion, matriz_registrado):
    print("*** Matriz asignación antes ***")
    mostrar_matriz(matriz_asignacion)
    print("*** Matriz registrado antes ***")
    mostrar_matriz(matriz_registrado)
    matriz_asignacion, matriz_registrado = revisar_matriz(matriz_asignacion, matriz_registrado)
    print("*** Matriz asignación después ***")
    mostrar_matriz(matriz_asignacion)
    print("*** Matriz registrado después ***")
    mostrar_matriz(matriz_registrado)
    eficiencia(matriz_asignacion, matriz_registrado)


controlDespachos([[1,5,0,10],[2,4,2,35],[3,1,1462,0],[4,3,1222,35],[5,2,2000,44],[6,3,1389,52],[7,1,1500,35],[8,1,1419,50],[9,5,1355,44],[10,4,1000,36]],
    [[1,5,1168,52],[2,4,1224,51],[3,1,1379,33],[4,3,1281,52],[5,2,1200,38],[6,3,1320,34],[7,1,1225,52],[8,1,1149,51],[9,5,1424,34],[10,4,1000,36]])