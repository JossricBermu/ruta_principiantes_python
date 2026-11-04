courses = (
#      0         1        2           3            4         5
    "Python", "Django", "Ruby", "Ruby on Rails", "MySQL", "MongoDB"
)

# var1 = courses[0]
# var2 = courses[1]
# var3 = courses[2]
# var4 = courses[3]
# var5 = courses[4]

# _
# var1, var2, var3, var4, var5 = "Python", "Django", "Ruby", "Ruby on Rails", "MySQL"

# var1, _, var3, var4, var5, _ = courses
# var1, var2, *sub_courses, _, last_value = courses
# 
# print(
#     var1, var2, sub_courses, last_value  
# )

var1, var2, *_, last_value = courses

print(
    var1, var2, last_value  
)
