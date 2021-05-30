# EJERCICIO 1.
# Definir un algoritmo en python que evalúe si una palabra o frase 
# es palíndromo; es decir, palabras que tienen el mismo aspecto escritas 
# invertidas. Ejemplo: ("radar") tendría que devolver True.

palabra = input("Ingrese una palabra: ")
palabra = palabra.replace(" ", "")
invertida = palabra[::-1]
print("Palabra ingresada: ", palabra)
print("Palabra invertida: ", invertida)

if palabra == invertida:
    print("La palabra ingresada es un palíndromo.")
else:
    print("La palabra ingresada no es un palíndromo.")