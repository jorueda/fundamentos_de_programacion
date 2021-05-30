def saludo(nombre):
    print(f"¡Hola {nombre}!")
    print("Bienvenido a Mision TIC 2022")

nom = input("Digite su nombre: ")
saludo(nom)
saludo("Karla")

def promedio(x, y):
    promedio = (x + y) / 2
    return promedio

a = 850
b = 570
media = promedio(a, b)
print("El promedio es:", media)
print("Programa terminado.")
