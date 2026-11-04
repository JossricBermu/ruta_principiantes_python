#             0         1         2       3         4
#            -5         -4       -3      -2        -1
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

# copy
# reverse
# sort

copy_list = courses.copy() # courses[:] # shallow copy
print(copy_list)

# reverse_list = courses[::-1]
# print(reverse_list)

courses.reverse()
print(courses)

courses.sort()
print(courses)

courses.sort(reverse=True)
print(courses)
