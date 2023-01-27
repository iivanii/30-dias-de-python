#1. Declare your age as integer variable
age = 16

#2. Declare your height as a float variable
height = 1.83

#3. Declare a variable that store a complex number
complex (2,3)

#4. Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
base=int(input('Dame una base cualquiera para un triángulo: '))
altura= int(input('Dame una altura cualuiera para triángulo: '))
area_triángulo= base*altura/2
print("El area de un triángulo cuya base es", base, "y cuya altura es", altura,"es", area_triángulo)

#5. Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
side_a=int(input('Dame el lado "a" de un triángulo: '))
side_b=int(input('Dame el lado "b" de un triángulo: '))
side_c=int(input('Dame el lado "c"de un triángulo: '))
perimeter=side_a+side_b+side_c
print ('El perímetro de un triángulo cuyos lados miden', side_a,',', side_b,'y', side_c, 'es', perimeter)

#6. Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
lenght_rectangle= int(input('Dame la altura de un rectángulo: '))
width_rectangle=int(input('Dame la anchura de un rectángulo: '))
area=lenght_rectangle*width_rectangle
perimeter= 2*(lenght_rectangle+width_rectangle)
print('Para un rectángulo de altura', lenght_rectangle,'y de anchura',width_rectangle,',','su area es',area,'y su perímetro es',perimeter)

#7. Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
radius_circle=int(input('Dame el radio de un círculo: '))
pi=3.14
area_circle=pi*radius_circle**2
circunference= 2*pi*radius_circle
print('Para un círculo cuyo radio es',radius_circle,'tiene como area',area_circle,'y como circunferencia',circunference)

#8. Calculate the slope, x-intercept and y-intercept of y = 2x -2
x= int(input('Dame "x": '))
y= 2*x-2
print('La pendiente cuando "x"','es',x,'en la ecuación "y=2*',x,'-2"','es',y)

#9. Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
import math
x1=2
x2=6
y1=2
y2=10
slope= y2-y1/x2-x1
print (slope)
d= math.sqrt(((x2-x1)**2 + (y2-y1)**2))
print (d)

#10. Compare the slopes in tasks 8 and 9
print('Primera pendiente: ',y)
print('Segunda pendiente: ',m)

#11. Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0


