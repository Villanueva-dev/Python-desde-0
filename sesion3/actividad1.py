"""
FizzBuzz
 1. Si el numero es divisible por 3: Imprimir "Fizz"
 2. Si el numero es divisible por 5: Imprimir "Buzz"
 3. Si el punto 1 y 2: Imprimir "Fizzbuzz"
"""

for a in range(1, 25):
    if a % 3 == 0 and a % 5 == 0:
        print(f"{a} FizzBuzz")
    elif a % 3 == 0:
        print(f"{a} Fizz")
    elif a % 5 == 0:
        print(f"{a} Buzz")
