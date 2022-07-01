# Exercise 1
# Create a list named studentscontaining some student names (strings).
# Print out the second student's name.
# Print out the last student's name.

students = ['David', 'Jquan', 'Iyana', 'Maika']
print(students[1])
print(students[2])

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

# Exercise 4
# Create a dictionary named home_towncontaining the keys of city, stateand population.
# Print a string with this format:
# "I was born in city, state - population of population"

home_town = {
    'city': 'Houston',
    'state': 'United States',
    'population': '2.3 million'
}
print(f"I was born in {home_town['city']}, {home_town['state']} - population of {home_town['population']} ")


# Exercise 5
# Iterate over the key: value pairs in home_townand print a string for each item, for example:

for key,val in home_town.items():
    print(f"{key} = {val}")

# Exercise 6
# Create an empty list named cohort.
# Using a forloop, add one dictionary to the cohortlist for each student name. Each dictionary should have this shape:

cohort=[]
if len (students) == len(foods):
    l = len(students)
    for i in range(l):
        cohort.append(
            dict(student=students[i], fav_foods=foods[i])
        )
        for student_dict in cohort:
            print(student_dict)

# Exercise 7
# Using the list of studentsand list comprehension, assign to a variable named awesome_studentsa new list containing strings similar to this:
# ["Tina is awesome!", "Fred is awesome!", "Wilma is awesome!"]
# Iterate over awesome_studentsprinting out each string.

awesome_students = [student + ' is awesome!' for student in students]
for a_student in awesome_students:
    print(a_student)

#     Exercise 8
# Using the tuple foodsand list comprehension within a forloop, print each food string that contains the letter a.

final= [key for key in foods if 'a' in key]
for each in final:
    print(each)