#             0         1         2       3         4
#            -5         -4       -3      -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)
new_courses = ["React", "Next"]

courses.append("Ruby on Rails")
courses.append("PHP")
courses.append("Laravel")

courses.insert(0, "Rust")
courses.insert(4, "C#")
courses.insert(2, "MySQL")

courses.extend(new_courses)

# print(
#     "Python" in courses
# )
# 
# print(
#     courses.index("Python")
# )

courses.remove("Python")
courses.remove("Django")

print("Python" in courses)

last_element = courses.pop() # retornar y expulsar el último elemento
print(last_element)

firt_element = courses.pop(0)
print(firt_element)

courses.clear() # Va a limpiar o resetear nuestra lista

print(courses)
print(len(courses))
