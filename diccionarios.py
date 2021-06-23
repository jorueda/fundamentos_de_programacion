diccionario = {
    'Nombre': 'Francisco',
    'Apellido': 'Castro',
    'Edad': 55,
    'email': 'fc@gmail.com',
    'casado': True
}

print(diccionario)
print(diccionario['email'])

print(diccionario.keys())

print(diccionario.values())

diccionario['Apellido'] = 'Morales'
print(diccionario)

print(len(diccionario))

print(diccionario.get('Edad'))