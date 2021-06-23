with open('alumnos.txt', 'r') as notas:
    # print(notas.read())
    # notas.seek(0)
    temporal = open('temporal.txt', 'w')
    aprobados = open('aprobados.txt', 'w')
    no_aprobados = open('no_aprobados.txt', 'w')
    for item in notas:
        datos = item.rstrip('\n').split(':')
        print(datos)
        suma = 0
        cantidad_notas = 3
        for posicion in range(2, 2 + cantidad_notas):
            suma += float(datos[posicion])
        promedio = round(suma / cantidad_notas, 2)
        nombre = datos[0] + datos[1] + ' '
        temporal.write(nombre + str(promedio) + '\n')
        if promedio >= 55:
            aprobados.write(nombre + str(promedio) + '\n')
        else:
            no_aprobados.write(nombre + str(promedio) + '\n')

    temporal.close()
    aprobados.close()
    no_aprobados.close()

print("*** Todas las notas ***")
with open('temporal.txt') as archivo:
    print(archivo.read())

print("*** Aprobados ***")
with open('aprobados.txt') as archivo:
    print(archivo.read())

print("*** No Aprobados ***")
with open('no_aprobados.txt') as archivo:
    print(archivo.read())
