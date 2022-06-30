# Exercise 1
# Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

# students = ['David', 'Jquan', 'Iyana', 'Maika']
# print(students[1])
# print(students[2])

# Exercise 2
# Create a tuple named foodscontaining the same number of foods (strings) as there are names in the studentslist.
# Use a forloop to print out the string "food goes here is a good food".

foods = ('Burger', 'Nachos', 'Cereal', 'Sushi')

for food in foods:
    print(f'{food} is a gooood food')


# Exercise 3
# Using a forloop, print just the last two food strings from foods.

for i in range(-1,-3,-1):
    print(f'{foods[i]}')

    