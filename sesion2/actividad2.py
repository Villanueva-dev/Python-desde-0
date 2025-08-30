""" 
Crea una función llamada devolver_distintos() que reciba 3 integers como parámetros

1. Si la suma de los 3 numeros es mayor a 15, va a devolver el número mayor

2. Si la suma de los 3 numeros es menor a 10, va a devolver el número menor

3. Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio
"""
def devolver_dintintos(num1, num2, num3):
    
    suma = num1 + num2 + num3
    lista_numeros = [num1, num2, num3]
    lista_numeros.sort()
    
    if suma > 15:
        mayor = lista_numeros[2]
        return mayor
    
    # Si la suma de los 3 numeros es menor a 10, va a devolver el número menor
    elif suma < 10:
        menor = lista_numeros[0]
        return menor
    
    # Si la suma de los 3 números es un valor entre 10 y 15(incluidos) va a devolver el número de valor intermedio
    elif suma >= 10 and suma <= 15:
        intermedio = lista_numeros[1]
        return intermedio
    
print(devolver_dintintos(9,3,5))
        
    


        
    
    
    
    
    