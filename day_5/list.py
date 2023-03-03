#1. Declare an empty list
list=[]
print(list)

#2. Declare a list with more than 5 items
list_5i=['computer', 'apple', 'mouse','table','chair', 'school','tree']
print(list_5i)

#3. Find the length of your list
length=len(list_5i)
print(length)

#4. Get the first item, the middle item and the last item of the list
print(list_5i[0])
print(list_5i[3])
print(list_5i[-1])

#5. Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types=['Iván', '16','1.83','single','Jerez']

#6. Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies=['Facebook','Google','Microsoft','Apple','IBM','Oracle','Amazon']

#7. Print the list using print()
print(it_companies)

#8. Print the number of companies in the list
print(len(it_companies))

#9. Print the first, middle and last company
print(it_companies[0])
print(it_companies[3])
print(it_companies[-1])

#10. Print the list after modifying one of the companies
it_companies[3]='Android'
print(it_companies)

#11. Add an IT company to it_companies
it_companies.append('Sony')
print(it_companies)

#12. Insert an IT company in the middle of the companies list
it_companies.insert(3, 'Activision')
print(it_companies)


#13. Change one of the it_companies item to uppercase
uppercase = it_companies[3].upper()
print(uppercase)

#14. Join the it_companies with a string '#;  '
join ='#,'.join(it_companies)
print(join)

# Check if a certain company exists in the it_companies list.
does_it_exist = 'apple' in it_companies
print(does_it_exist)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse=True)
print(it_companies)

# Slice out the first 3 companies from the list
firts_three_items = it_companies[0:3]
print(firts_three_items)


# Slice out the last 3 companies from the list
last_three_items = it_companies[6:]
print(last_three_items)

# Slice out the middle IT company or companies from the list
middle_item = it_companies[4:3]
print(middle_item)

# Remove the first IT company from the list
it_companies.remove('ujiigroceries')
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.remove('microsoft')
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies item
it_companies.clear()
print(it_companies)

# Destroy the IT companies list
del it_companies

# print(it_companies)

# Join the following lists:
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
full_stack = front_end + back_end
print(full_stack)

# After joining the lists in question 26. Copy the joined list and assigned it to a variable full_stack. Then insert, Python and SQL after Redux.
full_stack.append('python')
full_stack.append('SQL')
print(full_stack)

# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
print(ages)
min_age = 19
max_age = 26

# Add the min age and the max age
total_minmax_age = min_age + max_age
print(total_minmax_age)

# Find the median age(one middle item or two middle items divided by two)

# Find the average age(all items divided by number of items)
average_age = ages/2
print(average_age)

# Find the range of the ages(max minus min)
range_of_ages = max_age - min_age
print(range_of_ages)

# Compare the value of (min - average) and (max - average), use abs() method

# Find the middle country(ies) in the countries list

# Divide the countries list into two equal lists if it is even if not one more country for the first half.

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.