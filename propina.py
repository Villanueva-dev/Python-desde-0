""" 
Ejercicio 1: Propina
Crea un programa que calcule la propina a dejar en un restaurante. El programa debe solicitar al usuario el total de la cuenta y el porcentaje de propina que desea dejar. Luego, debe imprimir el monto de la propina y el total a pagar.
"""

sub_total = float(input("Digite el valor total a pagar: "))
porcentaje_propina =  float(input("Ingrese el porcentaje de propina: "))

valor_propina = sub_total / porcentaje_propina
valor_a_pagar = valor_propina + sub_total

print(f"El valor total a pagar es: {valor_a_pagar:.0f}")
