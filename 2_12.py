'''
To present list in concise and easy way we use List Comprehension. As size of the code is less, performance will be increased
'''
'''marks = [20, 35, 50, 78, 40]
new_marks = []  # Initialize an empty list
for x in marks:
    new_marks.append(x + 2)  # Add 2 to each element and append it to new_marks
print(new_marks)

#code using List Comprehension
marks = [20, 35, 50, 78, 40]
new_marks = [x + 2 for x in marks]  # List comprehension to add 2 to each element
print(new_marks)'''


"""x= [78,56,8,9,34] 
for a in x:
    print (a+2)
x=[78,56,8,9,34]
new_x=["""


'''Q.2) find Cube of even numbers'''

'''cubes=[]
for x in range (11):
    if x%2==0:
        cubes.append(x**3)
print("listing for loops", cubes)

#using list comprehension
easy=[x**3 for x in range (10) if x%2==0] 
print ("using List Comprehesion", easy)'''

# List comprehension for list
marks = [20, 35, 50, 78, 40]
new_marks = [x + 2 for x in marks]  # List comprehension
print(new_marks)

# Set comprehension for set
marks1 = {39, 25, 21, 56, 75}
new_marks1 = {x + 2 for x in marks1}  # Set comprehension
print(new_marks1)
