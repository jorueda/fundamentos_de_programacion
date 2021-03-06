# Ejercicio 1
# En este ejercicio deberás crear un script llamado personas.py que lea los datos de un fichero 
# de texto, que transforme cada fila en un diccionario y lo añada a una lista llamada personas. 
# Luego recorre las personas de la lista y para cada una muestra de forma amigable todos sus 
# campos. El fichero de texto se denominará personas.txt y tendrá el siguiente contenido en 
# texto plano (créalo previamente):

# 1;Carlos;Pérez;05/01/1989
# 2;Manuel;Heredia;26/12/1973
# 3;Rosa;Campos;12/06/1961
# 4;David;García;25/07/2006

lista = []
with open('personas.txt') as fichero:

    for item in fichero:
        datos = item.rstrip('\n').split(';')
        diccionario = {
            'id': datos[0],
            'nombre': datos[1],
            'apellido': datos[2],
            'nacimiento': datos[3]
        }
        print(diccionario)
        lista.append(diccionario)

    print("Id\tNombre\t\tApellido\tNacimiento")

    for item in lista:
        print(f"{item['id']}\t{item['nombre']}\t\t{item['apellido']}\t\t{item['nacimiento']}")
