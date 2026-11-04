#             0         1         2       3         4
#            -5        -4        -3      -2        -1
# slicing: [star:end:skips]
# slicings: [:] shadow copy
courses = ["Python", "Django", "Flask", "Ruby", "MongoDB"] # Strings (5)

# new_list = [
#     courses[0],
#     courses[1],
#     courses[2],
# ]
# 
# print(new_list)

new_list = courses[:3]
print(new_list)

new_list = courses[2:]
print(new_list)

# courses_copy = courses[:]
# print(courses_copy)

courses_copy = courses[::2]
print(courses_copy)

courses_copy = courses[::-1] # invertida
print(courses_copy)
