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
print(f'La longitud de la cadena "{sal}" es de {longitudString}') # Interpolacion utilizando f-string y {}

# 7. Recorrido
for i in range(longitudString):
    print(sal[i])

# 8. Mayusculas y Minusculas
salMayus = sal.upper()
print(salMayus)
salMinus = sal.lower()
print(salMinus)

# 9. Reemplazo
salReplace = sal
print(f'Palabra Original -> {salReplace}') # Interpolacion utilizando f-string y {}
salReplace = salReplace.replace("o", "2") # Reemplaza todas las "o" por un "2"
print(f'Primer reemplazo de letra "0" por un "2" -> {salReplace}') # Interpolacion utilizando f-string y {}
salReplace = salReplace.replace("2", "o", 1) # Reemplaza el primer "2" por una "o"
print(f'Segundo reemplazo, primer "2" por una "o" -> {salReplace}') # Interpolacion utilizando f-string y {}

# 10. Divison o Separacion
salDiv = sal
print(f'Palabra Original -> {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = salDiv.split(",") # Separa la cadena por el caracter "," y los deja en una lista
print(f'Separacion = {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = sal + " Me llamo Johan, soy ingeneriero electronico, me gusta el futbol, la programacion y la f1"
print(f'Otra separacion de la siguiente cadena -> {salDiv}') # Interpolacion utilizando f-string y {}
salDiv = salDiv.split(",", 2) # Separa por comas solo las dos primeras comas
print(f'Separacion = {salDiv}') # Interpolacion utilizando f-string y {}

# 11. Union
myStringList = ["uno", "dos", "tres", "cuatro"]
print(f'Lista -> {myStringList}') # Interpolacion utilizando f-string y {}
myString = ", ".join(myStringList)
print(f'Lista unida en un string -> {myString}') # Interpolacion utilizando f-string y {}
