# Demostración de trabajo con cadenas en Python

# Ejercicio 1: Introducción al tipo de dato string (cadena)
miCadena = "Esto es una cadena."
print(miCadena)
print(type(miCadena))
print(miCadena + " es del tipo de dato " + str(type(miCadena)))

# Ejercicio 2: Concatenación de cadenas
primeraCadena = "agua"
segundaCadena = "catarata"
terceraCadena = primeraCadena + segundaCadena
print(terceraCadena)

# Ejercicio 3: Entrada de usuario
nombre = input("¿Cuál es tu nombre? ")
print(nombre)

# Ejercicio 4: Formato de salida con múltiples entradas
color = input("¿Cuál es tu color favorito? ")
animal = input("¿Cuál es tu animal favorito? ")
print("{}, te gusta un {} {}!".format(nombre, color, animal))