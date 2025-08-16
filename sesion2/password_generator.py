import random

letras = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '{', '|', '}', '~']

usuario_letras = int(input("Cuantas letras desea en la contraseña?: "))
usuario_numeros = int(input("Cuantas numeros desea en la contraseña?: "))
usuario_simbolos = int(input("Cuantas simbolos desea en la contraseña?: "))

""" 
Via simple o sencilla: La contraseña se generará segun el orden de los inputs
Es decir: "pasgaovadpsa120456"!$&"
Via compleja: Independientemente del orden de los inputs se devuelve una contraseña en 
desorden: "pa0%4ov4dp$9a16"&"
"""
password = ""

for letra in range(1, usuario_letras + 1):
    password += random.choice(letras)
    
for numero in range(1, usuario_numeros + 1):
    password += random.choice(numeros)

for simbolo in range(1, usuario_simbolos + 1):
    password += random.choice(simbolos)
    
print(password)
