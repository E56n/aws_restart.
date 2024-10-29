import random

# Imprimir las reglas del juego
print("¡Bienvenido a Adivina el Número!")
print("Las reglas son simples. Yo pensaré en un número y tú intentarás adivinarlo.")

# Generar un número aleatorio entre 1 y 10
number = random.randint(1, 10)

# Variable para rastrear si la suposición es correcta
isGuessRight = False

# Bucle while para permitir múltiples intentos
while isGuessRight != True:
    guess = input("Adivina un número entre 1 y 10: ")
    
    # Verificar si la suposición es correcta
    if int(guess) == number:
        print("Adivinaste {}. ¡Eso es correcto! ¡Ganaste!".format(guess))
        isGuessRight = True
    else:
        print("Adivinaste {}. Lo siento, no es correcto. Intenta de nuevo.".format(guess))
