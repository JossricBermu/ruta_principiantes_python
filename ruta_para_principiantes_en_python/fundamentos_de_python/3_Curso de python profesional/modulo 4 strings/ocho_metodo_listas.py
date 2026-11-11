title = '  Curso profesional de Python!  '
print(title.strip())  # Elimina espacios en blanco al inicio y al final

print(title.upper())  # Convierte a mayúsculas
print(title.lower())  # Convierte a minúsculas

print(title.find('p')) # Busca la primera aparición de 'p' y devuelve su índice
print('105'.isnumeric())  # Verifica si la cadena es numérica

message = 'código facilito'
print(message.capitalize())  # Convierte la primera letra a mayúscula y el resto a minúscula

print(message[0].upper() + message[1:])  # Convierte la primera letra a mayúscula y concatena con el resto de la cadena
