
'''#while loop: loop is used to repeate particular block of sentence again and agai #it is advisable to use while loop if we don't know the stopping criteria
#WAP to print hello 10 times
i=1
#initialization
while (i<=10):
    print ("Hello")
    i+=1  #i=i+1

#WAP to generate table of a number
n=int(input ("Enter a number"))
i=1
while (i<=10):
    ans=n*i
    print (ans)  #i=i+1  '''


'''
# WAP to reverse a given number
n = int(input("Enter a number: "))  # Input a number from the user
rev = 0  # Initialize the reversed number to 0
while n > 0:
    rem = n % 10  # Get the last digit of the number
    rev = rev * 10 + rem  # Append it to the reversed number
    n = n // 10  # Remove the last digit from the number
print("The reverse of the given number is", rev)  # Output the reversed number

N=123
Iteration 1: n>0 123>0 T
Rem=123%10=3
Rev=rev*10+rem=0*10+3=3
N=n//10=123//10=12
Iteration 2:
12>0 T
Rem=12%10=2
Rev=3*10+2=32
N=12/10=1
Iteration:3
1>0 T
rem=1%10=1
rev=32*10+1=321
n=1/10=0
iteration 4
0>0 f   '''

'''
# WAP to reverse a given number
n = int(input("Enter a number: "))
temp = n  
rev = 0 
# Reverse the number
while n > 0:
    rem = n % 10  # Get the last digit of the number
    rev = rev * 10 + rem
    n = n // 10
print("The reverse of the given number is", rev)

# WAP to Check if the number is a palindrome
# n=434   rev=424 palindrome
if rev == temp:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")'''

# Program to calculate the sum of digits of a number entered by the user
# Input number from the user
n = int(input("Enter a number: "))
sum1 = 0

# Calculate the sum of digits
while n > 0:
    rem = n % 10      # Get the last digit
    sum1 += rem       # Add it to the sum
    n = n // 10       # Remove the last digit

print("The sum of digits is:", sum1)

