# Ejercicio 1: Trabajando con la declaración if
userReply = input("¿Necesitas enviar un paquete? (Ingresa sí o no) ")

if userReply.lower() == "si":
    print("¡Podemos ayudarte a enviar ese paquete!")
else:
    print("Por favor, vuelve cuando necesites enviar un paquete. Gracias.")

# Ejercicio 2: Trabajando con la declaración elif
userReply = input("¿Te gustaría comprar sellos, comprar un sobre o hacer una copia? (Ingresa sellos, sobre o copia) ")

if userReply == "sellos":
    print("Tenemos muchos diseños de sellos para elegir.")
elif userReply == "sobre":
    print("Tenemos muchos tamaños de sobres disponibles.")
elif userReply == "copia":
    copias = input("¿Cuántas copias te gustaría? (Ingresa un número) ")
    print("Aquí tienes {} copias.".format(copias))
else:
    print("Gracias, por favor vuelve pronto.")
