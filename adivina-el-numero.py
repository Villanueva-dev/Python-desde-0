""" 
Ejercicio2: 
- Crea un juego en el que la computadora elige un número al azar entre 1 y 100
El usuario tiene que adivinarlo. 
El programa debe dar pistas al usuario si:
    - su número es mayor o menor que el número secreto. 
    - El juego termina cuando el usuario adivina el número.
"""
from random import randint

numero_secreto = randint(1,100)
intentos = 1

while intentos <= 10:
    
    #Validacion para que no permita numeros decimales.
    numero_usuario = int(input("Ingrese el numero: "))
    if numero_usuario < 1 or numero_usuario > 100:
        if numero_usuario < numero_secreto:
            print(f"El {numero_usuario} es menor al número secreto")
            intentos += 1
        elif numero_usuario > numero_secreto:
            print(f"El {numero_usuario} es mayor al número secreto")
            intentos += 1
        elif numero_usuario == numero_secreto:
            print(f"Felicidades. Adivinaste el numero: {numero_secreto}")
            break
        else:
            print("ERROR. Intente de nuevo")


