students = { 
'Alice': 85,
'Bob': 92,  
'Charlie': 78,
'John': 56,
'Elias': 99,
'Kok Seng': 65
}

# grade = input('What is ur name?')

# print(students[grade])

# students["Dom"] = 5 
# students['John'] =7
# del students['Kok Seng']

# inputstu = input('hi')

# if inputstu in students:
#     print(inputstu + 'in dictionary')
# else:
#     print(inputstu + 'not in dictionary')

# print(students)


#loop through the dictionary
for name,grade in students.items():
    print(name,grade)
