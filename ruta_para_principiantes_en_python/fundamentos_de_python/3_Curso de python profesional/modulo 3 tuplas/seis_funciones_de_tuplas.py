numbers = (
    1, 4, 5, 3, 3, 7, 2, 10
)

print(
    len(numbers)
)

print(
    sorted(numbers) # list (difault=acs)
)

print(
    sorted(numbers, reverse=True) # list (en forma desendiente)
)

print(numbers.count(3)) # Cuenta las veces que aparece el valor

print(
    3 in numbers     # Para verificar si un valor se encuentra dentro de la tupla
)

print(
    numbers.index(4) # Para conocer exactamente en qué indice se encuentra el valor
)
