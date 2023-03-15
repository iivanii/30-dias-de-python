#Level 1
#1. Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
Age=int(input('Determina tu edad: '))
if Age < 18:
    print('Te faltan',18-Age,'año(s) para poder conducir')
else:
    print('Cumples los requisitos de edad adecuados para conducir')

#2. Compare the values of my_age and your_age using if … else. Who is older (me or you)? Use input(“Enter your age: ”) to get the age as input. You can use a nested condition to print 'year' for 1 year difference in age, 'years' for bigger differences, and a custom text if my_age = your_age.
my_age=16
print('Tengo',my_age,'años')
your_age=int(input('Introduce tu edad: '))
if your_age < my_age:
    print('Soy', my_age-your_age,'año(s) mayor que tú')
else:
    print('Eres',your_age-my_age,'año(s) mayor que yo')

#3. Get two numbers from the user using input prompt. If a is greater than b return a is greater than b, if a is less b return a is smaller than b, else a is equal to b.
a=(input('Asígnale un valor a un número "a": '))
b=(input('Asígnale un valor a un número "b": '))
if a < b:
    print(b,'es mayor que',a)
elif a > b:
    print(a,'es mayor que',b)
else:
    print(a,'es igual a',b)

#Level 2

#1. Write a code which gives grade to students according to theirs scores:
puntaje=int(input('Nota del alumno: '))
if puntaje > 80 < 100:
    print('A')
elif puntaje > 70 < 80:
    print('B')
elif puntaje > 60 < 70:
    print('C')
elif puntaje > 50 < 60:
    print('D')
else:
    print('F')

#2. Check if the season is Autumn, Winter, Spring or Summer. If the user input is: September, October or November, the season is Autumn. December, January or February, the season is Winter. March, April or May, the season is Spring June, July or August, the season is Summer
estación=input('Mes actual: ').capitalize()

if estación=='Enero' or estación=='Febrero' or estación== 'Diciembre':
    print('Es invierno')
elif estación=='Marzo' or estación== 'Abril' or estación== 'Mayo':
    print('Es primavera: ')
elif estación=='Junio' or estación== 'Julio' or estación== 'Agosto':
    print('Es verano')
else:
    print('Es otoño')

#3. The following list contains some fruits: fruits = ['banana', 'orange', 'mango', 'lemon']. If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists print('That fruit already exist in the list')
fruits=['banana','orange','mango','lemon']
usufruits=input('Nombra una fruta: ')
existe=usufruits in fruits
if existe==False: 
    fruits.append(usufruits)
    print(fruits)
else:
    print('Esta fruta ya existe en la lista')

