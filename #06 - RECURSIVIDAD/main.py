###################################
# Dev: rianojnicolas              #
###################################

# EJERCICIO:
# función recursiva que imprima números del 100 al 0.
def print_numbers(n):
    if n >= 0:
        print(n)
        print_numbers(n-1)

print_numbers(100)  # Imprime los números del 100 al 0


