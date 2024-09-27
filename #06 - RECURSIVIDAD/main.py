###################################
# Dev: rianojnicolas              #
###################################

# EJERCICIO:
# función recursiva que imprima números del 100 al 0.
def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n-1)

# print_numbers(100)  # Imprime los números del 100 al 0

# DIFICULTAD EXTRA:
# 1. Factorial de un numero n
def calc_factorial(n):
    if n == 0:
        return 1
    else:
        return n*calc_factorial(n-1)

print(calc_factorial(5))  # Imprime el factorial de 5
