""" 
Piedra, papel o tijera
Reglas del juego:
1. Piedra gana a tijera
2. Tijera gana a papel
3. Papel gana a piedra
4. Si ambos eligen lo mismo: Empate

Como el usuario elige la opcion
Validar que las reglas del juego se cumplan con condicionales
"""

"""if opcion_usuario == "tijera" and opcion_maquina == "papel":
        puntaje += 1
    elif opcion_usuario == "piedra" and opcion_maquina == "tijera":
        puntaje += 1
    elif opcion_usuario == "papel" and opcion_maquina == "piedra":
        puntaje += 1
    else: 
        print("Perdiste. La maquina ganó")"""

import random 

opciones = ["piedra", "papel", "tijera"]

puntaje = 0

while puntaje < 3:
    
    print("Bienvenid@ a Piedra, papel o tijera")
    
    opcion_maquina = random.choice(opciones)
    
    opcion_usuario = input("Piedra, papel o tijera? ").strip().lower()
    
    if opcion_usuario == opcion_maquina:
        print("Empate\n")
        continue
    
    if(opcion_usuario == "tijera" and opcion_maquina == "papel") or (opcion_usuario == "piedra" and opcion_maquina == "tijera") or (opcion_usuario == "papel" and opcion_maquina == "piedra"):
        puntaje += 1
        print(f"Ganaste esta ronda {puntaje} | Elegiste: {opcion_usuario} y la maquina: {opcion_maquina}\n")
    else: 
        print(f"Perdiste. Elegiste: {opcion_usuario} y la maquina: {opcion_maquina}\n")

print("Felicidades por ganar el juego")
        