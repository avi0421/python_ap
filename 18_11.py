'''
Ordered:
When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
Unchangeable: Tuples are unchangeable, meaning that we cannot change, add or items after the tuple has been created.
Allow Duplicates:
Since tuples are indexed, they can have items with the same value:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple))
print(thistuple[0])
print(thistuple[3])
print(thistuple[2:4])



tuple1=("Aaa", 78, "O grade", 56000,"navi mumbai") 
print (tuple1)

print (type (tuple1))

# slicing a tuple
print (tuple1 [1:4])
print (tuple1 [2:])
print (tuple1 [:5])

# negative indexing
print (tuple1 [-2])
print (tuple1 [-1])

# tuple1[1]=89
# print(tuple1) #cant change tuple

#note
t1=("Aditya", 35, 78, "O grade", 35) 
print (type (t1)) 
print (t1)
#tuple slicing
print (t1 [1:])
print (t1[:3])
print (t1[1:3])
#find length of the tuple
print ("The length of the tuple is: ", len (t1))
#you can also give negative indexing.
print (t1 [-2])
print (t1 [-1])
#Note:
#List is a collection which is ordered and changeable. 
#List Allows duplicate members.
#Tuple is a collection which is ordered and unchangeable. 
#Tuple Allows duplicate members.


t2-list (t1) 
print (t2)
t2 [2]="A in sports" 
print (t2)
for i in t2: print (i)
'''


# Reverse the given tuple
tup1 = (56, 78, 34, 89, 8)
print("The original tuple is:", tup1)
res = tup1[::-1]  # Reverse the tuple using slicing
print("The reverse order is:")
print(res)

# Print even numbers in the tuple
for i in tup1:
    if i % 2 == 0:
        print(i)

# Working with nested tuple
tup2 = (45, [34, 89], 80, 73, 45, 45, 90)
print(tup2[0])  # Prints the first element
print(tup2[1])  # Prints the second element, which is a list
print(tup2[1][0])  # Prints the first element of the second element (list)
print(tup2[1][1])  # Prints the second element of the second element (list)

# Modifying an element inside the list (which is mutable)
tup2[1][0] = 45
print(tup2)  # Prints the modified tuple

#WAP to count the 45 in tuple
print("The 45 occurs ",tup2.count(45),"times")
'''tuple can not be changed
tup2[2]=78
print(tup2)
'''
#WAP to create tuple with different data types
my_tuple=("Maggi",3,15.5,True)
print("I want to eat Maggi",my_tuple)

marks=23,67,87,34
print("I have got marks as:")
print(marks)

#WAP to create tuple with single item
price=34,
print(price)