#Level 1
#1. Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers (a,b):
    return a + b
print (add_two_numbers(5,10))

#2. Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle (r):
    return 3.14 * r * r
print (area_of_circle(5))

#3.
def add_all_nums (*nums):
    sum_of_nums = 0
    for i in nums:
        if isinstance(i, int):
            sum_of_nums += i
    return sum_of_nums
print (add_all_nums(30,40,50))

#4.
def convert_celsius_to_fahrenheit (celsius):
    return (celsius*9/5) + 32
print (convert_celsius_to_fahrenheit(28))

#5.
def check_season(month):
    if month in ['September', 'October','November',]:
        print('Autum')
    if month in ['December','January','February']:
        print('Winter')
    if month in ['March','April','May']:
        print('Spring')
    else:
        print('Summer')
print(check_season('July'))

#8.
def print_list (lst):
    for i in lst:
        print(i)
print(print_list('hello'))

#9. 
def reverse_list (a):
    return a [::-1]
print(reverse_list([1,2,3,4,5]))

#10.
def capitalize_list_items(lst):
    result=[]
    if(len(lst)>0):
        for l in lst:
            if(isinstance(l,str)):
                result.append(l.capitalize())
    return  result
print(capitalize_list_items(['pineaple','apple','banna','watermelon']))

#11. 
def add_item (lst,item):
    if(isinstance(lst,list)):
        if(item!=None):
            lst.append(item)
    return lst
food_staff=['Potato','Tomato','Mango','Milk']
print(add_item(food_staff,'Meat'))
numbers = [2,3,7,9]
print(add_item(numbers,5))

#12.
def remove_item (lst,item):
    if (isinstance(lst,list)) and len(lst) > 0:
        if (item!=None):
            lst.remove(item)
    return lst
food_staff=['Potato','Tomato','Mango','Milk']
print(remove_item(food_staff,'Mango'))
numbers = [2,3,7,9]
print(remove_item(numbers,3))

#13. 
def sum_of_numbers(num):
    sum=0
    if (num>0):
        for i in range(1,num+1):
            sum+=i
    return sum
print(sum_of_numbers(5))
print(sum_of_numbers(10))
print(sum_of_numbers(100))

#Level 3

#1. 
def is_prime (num):
    flag = True
    if (type(num)is int):
        if(num >1):
            for i in range(2,int(num/2)+1):
                if(i%2==0):
                    flag==False
                    break
        else:flag=False
    else:flag=False
    return flag
print(is_prime(2))

#2.
def is_unique(lst):
    test_set=set()
    test_set=set()
    if (len(test_set)==len(lst)):
        return True
    return False
list1=[1,2,3,4]
list2=[1,2,3,4,]
print(is_unique(list1))
print(is_unique(list2))

