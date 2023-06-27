# saludo-edad
# obtener el nombre del usuario
nombre = input("Nombre: ")

# Obtener el apellido del usuario
apellido = input("Apellido: ")

# Obtener la edad del usuario
edad = int(input("Edad: "))

# Calcular el año de nacimiento
año_actual = 2023
año_nacimiento = año_actual - edad

# Imprimir el saludo y el año de nacimiento
print("Hola", nombre, apellido + ",", "naciste en", str(año_nacimiento))
