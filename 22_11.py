'''
#function is self contained block of statement which has specific task to perform #same block of code can be reused whenever required
def myfunction():
    print ("Hello all to the world of struggle")
    myfunction ()

def add(a,b):
    c= a+b
    print ("The addition is ", c)

a=int(input ("Enter first number: "))
b=int(input ("Enter second number: "))
add (a, b )


# WAP to get Area of Rectangle
def area_of_rectangle(length, breadth):
    return length * breadth

length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
print(f"The area of the rectangle is: {area_of_rectangle(length, breadth)}")

# WAP to get Area of circle
def area_of_circle(radius):
    pi = 3.14159
    return pi * radius ** 2

radius = float(input("Enter the radius of the circle: "))
print(f"The area of the circle is: {area_of_circle(radius)}")

# WAP to remove duplicates from the list
def remove_duplicates(lst):
    return list(set(lst))

original_lst = input("Enter elements of the list separated by space: ").split()
print(f"The list after removing duplicates: {remove_duplicates(original_lst)}")
'''

# WAP to get factorial of a number using recursion and without using any built-in function in python.
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

n = int(input("Enter the number: "))
ans = factorial(n )
print("The factorial of",n,"is" , ans)

'''
n=5
fact=5*4*3*2*1=120
5*factorial (4)
5*4*factorial (3)
5*4*3*factorial (2)
5*4*3*2* factorial (1) 
5*4*3*2*1* factorial (0) 
5*4*3*2*1*1
'''

'''
Average of 11
(x1+x2+x3+...+x11)/11=30
Sum of 11 num=30*11=330
(X1+.....+x6)/6=17.5
Sum of first six=17.5*6=105
(X6+...+x11)/6=42.5
Sum=255
Total=sum of six+sum of last six
330=105+255-360
360-330=30'''