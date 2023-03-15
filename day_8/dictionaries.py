#1. Create an empty dictionary called dog
dog={}

#2. Add name, color, breed, legs, age to the dog dictionary
dog['Name']='Iván'
dog['Color']='Red'
dog['Breed']='Border_Collie'
dog['Legs']=4
dog['Age']=9

#3. Create a student dictionary and add first_name, last_name, gender, age, marital status, skills, country, city and address as keys for the dictionary
student={
    'first_name':'Paco',
    'last_name':'Parra',
    'gender':'Male',
    'age':'17',
    'marital status':'single',
    'skills':['to read','to run','basketball','mats'],
    'country':'Spain',
    'City and address': 'Jerez, El Rosal',
}

#4. Get the length of the student dictionary
len(student)

#5. Get the value of skills and check the data type, it should be a list
skills=student['skills']
print(skills)
print(type(skills))

#6. Modify the skills values by adding one or two skills
student['skills']='baseball'
print(student)

#7. Get the dictionary keys as a list
print(student.keys())

#8. Get the dictionary values as a list
print(student.values())

#9. Change the dictionary to a list of tuples using items() method
dictionary_list=student.items()

#10. Delete one of the items in the dictionary
print(student.pop('skills'))

#11. Delete one of the dictionaries 
del student

