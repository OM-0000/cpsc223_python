#So, here is a case where you might want to use nesting
student1_dict = {
    'name': 'Jim Bob',
    'id': 123456,
    'schedule': 'CPSC223p, ENG1, MATH2',
}

print(student1_dict)

student1_dict = {
    'name': 'Jim Bob',
    'id': 123456,
    'schedule': ['CPSC223p', 'ENG1', 'MATH2',]
}

print(student1_dict)
print(student1_dict['schedule'])
print(student1_dict.get('schedule')[0])
for myclass in student1_dict['schedule']:
    print(f"The class is {myclass}")

