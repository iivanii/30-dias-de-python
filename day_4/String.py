#1. Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
Thirty='Thirty'
Days='Days'
Of='Of'
Python='Python'
espace=' '
Thirty_Days_Of_Python=Thirty+espace+Days+espace+Of+espace+Python
print(Thirty_Days_Of_Python)

#2. Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
Coding='Coding'
For='For'
All='All'
Coding_For_All=Coding+espace+For+espace+All
print(Coding_For_All)

#3. Declare a variable named company and assign it to an initial value "Coding For All".
company=Coding_For_All

#4. Print the variable company using print().
print(company)

#5. Print the length of the company string using len() method and print().
print(len(company))

#6. Change all the characters to uppercase letters using upper() method.
mayus=company.upper()
print(mayus)

#7. Change all the characters to lowercase letters using lower() method.
minus=company.lower()
print(minus)

#8. Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
capitalize=company.capitalize()
print(capitalize)
title=company.title()
print(title)
swapcase=company.swapcase()
print(swapcase)

#9. Cut(slice) out the first word of Coding For All string.
cut=slice(0,6)
print(company[cut])

#10. Check if Coding For All string contains a word Coding using the method index, find or other methods.
index='Coding'
print(company.index(index))

find='Coding'
company.find(find)
print(find)

#11. Replace the word coding in the string 'Coding For All' to Python.
replace=company.replace('Coding','Python')
print(replace)

#12. Change Python for Everyone to Python for All using the replace method or other methods.
replace_2=replace.replace('All','Everyone')
print(replace_2)

replace_2=replace.replace('All', 'Everyone')
print(replace_2)

#13. Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
servicios_informáticos=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(servicios_informáticos)

#15. What is the character at index 0 in the string Coding For All.
print (company[0])

#16. What is the last index of the string Coding For All.
print(company[-1])

#17. What character is at index 10 in "Coding For All" string.
print(company[10])

#18. Create an acronym or an abbreviation for the name 'Python For Everyone'.
PFE= 'Coding For Everyone'
print (''.join(w[0] for w in PFE.split()))

#19. Create an acronym or an abbreviation for the name 'Coding For All'.
CFA= company
print (('').join(w[0] for w in CFA.split()))

#20. Use index to determine the position of the first occurrence of C in Coding For All.
print(company.index('C'))

#21. Use index to determine the position of the first occurrence of F in Coding For All.
print(company.index('F'))

#22. Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind('l'))

#23. Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
because='You cannot end a sentence with because because because is a conjunction'
print(because.index('because'))

#24. Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(because.rindex('because'))

#25. Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
slice1=because[0:31]
slice2=because[55:71]
print(slice1+slice2)

