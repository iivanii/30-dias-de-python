#Level 1
#1. Iterate 0 to 10 using for loop, do the same using while loop.
count = 0
while count < 11:
    print(count)
    count = count + 1

#2. Iterate 10 to 0 using for loop, do the same using while loop.
count1 = 10
while count1 > -1:
    print(count1)
    count1 = count1 -1

#3. Write a loop that makes seven calls to print(), so we get on the output the following triangle:
for i in range(0,7):
    for n in range(0,i+1):
        print('# ',end='')
    print('\r')

#4. Use nested loops to create the following:
for i in range(0,8):
    for n in range(0,8):
        print('# ',end='')
    print ('\r')
print(' ')

#5. Print the following pattern:
for i in range (0,11):
    print(i,"x",i,"=",i*i)

#6. Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
for lang in ['Python','Numpy','Pandas','Django','Flask']:
    print(lang)

#7. Use for loop to iterate from 0 to 100 and print only even numbers
for i in range (0,101):
    if i % 2 == 0:
        print(i)
print(' ')

#8. Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range (0,101):
    if i % 2 != 0:
       print(i)
print(' ')

#Level 2

#1. Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum_nums = 0
for i in range (0,101):
    sum_nums += i
print('The sum of all numbers is',sum_nums)

#2. Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
even_sum= 0
odd_sum = 0
print(' ')
for i in range (0,101):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i
print('The sum of all even numbers is', even_sum)
print ('The sun of all odd numbers is',odd_sum)
print(' ')

#3. Go to the data folder and use the countries.py file. Loop through the countries and extract all the countries containing the word land.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
]
list_c=countries
for country in list_c:
    if 'land' in country:
        print(country)
fruits = ['banana', 'orange', 'mango','lemon']
rev=[]
for i in range(3,-1,-1):
    rev.append(fruits[i])
print(rev)