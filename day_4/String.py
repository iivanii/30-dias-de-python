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
replace_2=replace.replace('All', 'Everyone')
print(replace_2)

#13. Split the string 'Coding For All' using space as the separator (split()).
print(company.split())

#14. "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
servicios_informáticos=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']
print(servicios_informáticos)

