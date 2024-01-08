# Operadores Aritmeticos

a = 1
b = -2
print("OPERADORES ARITMETICOS")
suma = a + b 
print(f'La suma entre {a} y {b} es igual a {suma}')
resta = a - b
print(f'La resta entre {a} y {b} es igual a {resta}')
division = a/b
print(f'La division entre {a} y {b} es igual a {division}')
producto = a*b
print(f'La multiplicacion entre {a} y {b} es igual a {producto}')
potencia = a**b
print(f'El numero {a} elevado a la potencia {b} es igual a {potencia}')
modulo = a%b
print(f'El resto de la division entre {a} y {b} es igual a {modulo}')
print("")

# Operadores Relacionales
print("OPERADORES RELACIONALES")
igualdad = a == b
print(f'¿ Son iguales {a} y {b} ? RTA -> {igualdad}')
diferencia = a != b
print(f'¿ Son diferentes {a} y {b} ? RTA -> {diferencia}')
mayor = a > b
print(f'¿ {a} es mayor a {b} ? RTA -> {mayor}')
menor = a < b
print(f'¿ {a} es menor a {b} ? RTA -> {menor}')
menorIgual = a <= b
print(f'¿ {a} es menor e igual a {b} ? RTA -> {menorIgual}')
mayorIgual = a >= b
print(f'¿ {a} es mayor e igual a {b} ? RTA -> {mayorIgual}')
print("")

# Operadores de Asignacion
print("OPERADORES DE ASIGNACION")
asignar = 1
print(f'a la variable **asignar** le asigne el valor de {asignar}')
print("")
print("CONTADOR DE SUMA (a += 1), SUMANDO + 1")
while(a<5):
    a += 1
    print(f'contador +1 iniciando en 1, el resultado es {a}')
print("")
print("CONTADOR DE RESTA (a -= 1), RESTANDO -1")
while(b>-5):
    b -= 1
    print(f'contador -1 iniciando en {-2}, el resultado es {b}')
print("")
print(
    """
    Tambien existen los contadores de tipo 
    (a *= 1), (a /= 1), (a %= 1) y (a **= 1),
    Teniendo en cuenta que el numero 1 se puede
    reemplazar por cualquier numero o por otra variable.
    """)
print("")

# Operadores Logicos
A = True
B = False
print("OPERADORES LOGICOS")
# AND
print(f'{A} and {B} = {A and B}')
print(f'{B} and {A} = {B and A}')
print(f'{A} and {A} = {A and A}')

# OR
print(f'{B} or {A} = {B or A}')
print(f'{A} or {B} = {A or B}')
print(f'{A} or {A} = {A or A}')
print(f'{B} or {B} = {B or B}')

# NOT
print(f'not({A}) = {not A}')
print(f'not({B}) = {not B}')
print("")

# Operadores de Pertenencia
print("OPERADORES DE PERTENCIA")


