# Definir una lista con diferentes tipos de datos
myMixedTypeList = [45, 290578, 1.02, True, "My dog is on the bed.", "45"]

# Recorrer la lista e imprimir el tipo de dato de cada elemento
for item in myMixedTypeList:
    print("{} is of the data type {}".format(item, type(item)))
