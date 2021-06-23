import csv
import json

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open('contactos1.csv', 'w') as csvfile:
    escritor = csv.writer(csvfile)
    for item in contactos:
        escritor.writerow(item)

print("*** Archivo CSV ***")
with open('contactos1.csv') as csvfile:
    lector = csv.reader(csvfile)
    for nombre, empleo, email in lector:
        print(nombre, empleo, email)

with open('contactos2.csv', 'w') as csvfile:
    titulos = ['Nombre', 'Empleo', 'Email']
    escritor = csv.DictWriter(csvfile, fieldnames=titulos)
    escritor.writeheader()
    for nombre, empleo, email in contactos:
        escritor.writerow({
            'Nombre': nombre,
            'Empleo': empleo,
            'Email': email
        })

print("*** Archivo Diccionarios ***")
with open('contactos2.csv') as csvfile:
    lector = csv.DictReader(csvfile)
    for item in lector:
        print(item['Nombre'], item['Empleo'], item['Email'])

lista = []
for nombre, empleo, email in contactos:
    lista.append({
            'Nombre': nombre,
            'Empleo': empleo,
            'Email': email
        })

with open('contactos3.json', 'w') as jsonfile:
    json.dump(lista, jsonfile)

print("*** Archivo JSON ***")
with open('contactos3.json') as jsonfile:
    fila = json.load(jsonfile)
    for item in fila:
        print(item['Nombre'], item['Empleo'], item['Email'])