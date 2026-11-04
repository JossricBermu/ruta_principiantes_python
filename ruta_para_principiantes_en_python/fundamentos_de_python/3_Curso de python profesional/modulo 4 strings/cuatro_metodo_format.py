name = 'Eduardo'
last_name = 'García'

# 4 - format
base = 'El nombre completo es: {} {}. Su edad es: {}'
full_name = base.format(name, last_name, 30)
print(full_name)

'''name = input('Ingresa tu nombre: ')
last_name = input('Ingresa tu apellido: ')
age = input('Ingresa tu edad: ')
full_name = base.format(name, last_name, age)
print(full_name)'''

base = 'El nombre completo es: {name} {last_name}. Su edad es: {age}. Active: {active}'
full_name = base.format(
    age=30,
    name=name,
    active = True,
    last_name=last_name,
)
print(full_name)
