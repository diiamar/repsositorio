# El factorial de un número entero positivo n (denotado como n!) es el producto de todos los enteros positivos menores o iguales a n. 
# Por ejemplo, 5! = 5 * 4 * 3 * 2 * 1 = 120.

# Crea un programa en Python que resuelva dicho problema matemático de una forma RECURSIVA.

def factorial(n):
    if not n:
        return 1
    else: 
        return n * factorial(n-1)

resultado=factorial(5)
print(resultado)