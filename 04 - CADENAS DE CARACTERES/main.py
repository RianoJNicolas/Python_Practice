# OPERACIONES CON CADENAS DE CARACTERES

# 1. Asignacion
saludo = "Hola, "
nombre = "Nico"

# 2. Concatenacion
sal = saludo + nombre
print(sal)

# 3. Operaciones "aritmeticas"
saludoTotal = saludo*3
print(saludoTotal)

# 4. Operaciones de partcion (Subcadena)
secuencia = "123456789"
primerCorte = secuencia[0:2:1] # Se toma -> 12
segundoCorte = secuencia[::2] # Se toma -> 13579
tercerCorte = secuencia[::3] # Se toma -> 147 
cuartoCorte = secuencia[::] #Se toma toda la cadena
print(primerCorte)
print(segundoCorte)
print(tercerCorte)
print(cuartoCorte)

# 5. Acceso a caracteres
caracter1 = sal[0]
caracter2 = sal[4]
print(caracter1)
print(caracter2)

# 6. Longitud
longitudString = len(sal)
print(f'La longitud de la cadena "{sal}" es de {longitudString}')

# 7. Recorrido
for i in range(longitudString):
    print(sal[i])

# 8. Mayusculas y Minusculas
salMayus = sal.upper()
print(salMayus)
salMinus = sal.lower()
print(salMinus)