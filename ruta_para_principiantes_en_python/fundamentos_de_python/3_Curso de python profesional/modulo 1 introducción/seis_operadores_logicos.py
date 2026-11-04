# and, or, not

number_one = 10
number_two = 20

result = (
    True 
    and True 
    and number_one != number_two 
    and number_one < 100 
    and number_two > 200
    )
print(result)

result_two = (
    False 
    or False 
    or number_one == number_two 
    or number_one < 100 
    or number_two > 200
    )
print(result_two)

print(not not not result_two)

result_three = not (
    (number_one == number_two and True)
    and (number_one < 100)
    and (number_two < 100)
    or (number_one > 100 and number_two > 200)
)

print(result_three)
