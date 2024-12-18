'''# wap to generate squares between 10 and 20

for i in range(10, 21):
    ans = i* i
    print("square is:",ans) '''

'''# wap to generate even no. between 1 and 20
start = int(input("Enter the starting value: "))

print(f"Even numbers between {start} and 20 are:")
for i in range(start, 1001):
    if i % 2 == 0:
        print(i)'''

'''start = int(input("Enter the starting range of the number: "))
end = int(input("Enter the ending range of the number: "))
for i in range(start, end + 1):
    if i % 2 == 0:
        print(i)'''

'''sum1 = 0
for i in range (1,11):
    sum1 = sum1+i
    print(sum1)
    print("The sum of 1st 10 natural nos is",sum1)'''

'''# wap to find factorial of a number
# 5! = 5*4*3*2*1
n=int(input("Enter a number:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
    print(fact)
print("factorial of",n,"is",fact)'''

'''#use of break statement
for i in range(1,25):
    if(i==15):
        break
    print("hello",i)
print("loop Exited")'''

'''#use of continue statement
for i in range(1,25):
    if(i==15):
        continue
    print("hello",i)
print("loop Exited")'''

import random #importing random module too generate  random numbers
# Simulating temperature readings
for i in range(1,11): #10 temperature readings
    temperature = random.randint(20,100)
    print(f"Reading {i}: Temperature = {temperature} °C")

    if temperature  > 70:
        print("Danger! High temperature detected. Stopping monitoring.")
        break # stop monitoring when temp exceeds safe limits