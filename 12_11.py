'''
#List is a collection which is ordered and changeable. 
# #Allows duplicate members.
my_list=["Soap", "Oil", "Maggie", "Tea", 345, "buiscuits", "rice"] 
print (my_list)
for i in my_list:
    print(i)
my_list.append("Dalia")
print(my_list)

#list element is recognized by its index value
#first element my_list[0]
print(my_list[0])
#there is concept of negative indexing
print(my_list[-1])

#slicing
print(my_list[1:4])
print(my_list[:])
print(my_list[2:])
print(my_list[:5])
print(my_list[::-1])#reversing
'''

marks=[34,56,23,89,54]
print (min (marks))
print ("The maximum value is", max (marks))

#WAP to find 2nd largest element
for i in range(0,5):
    for j in range(i+1,5):
        if marks[j]>marks[i]:
            temp=marks[i]
            marks[i]=marks[j]
            marks[j]=temp
print(marks)
print(marks[1])

'''
#Bubble sort
[34,56,23,89,54]
i=0

i=0       j=1
marks[0]=34
marks[1]=56
if 56>34  T       56 34 23 89 54
marks[2]>marks[0]
23>56     F
marks[3]>marks[0]
89>56     T       89 34 23 56 54
marks[4]>marks[0]
54>56     F

Iteration 2:
i=1          j=2
marks[1]=34   marks[2]=23

23>34     F
j=3
Marks[3]=56
56>34 t
89 56 23 34 54

J=4
Marks[4]=54
54>56 f

Iteration :3
Marks[2]=23 marks[3]=34
34>23 t
89 56 34 23 54
J=4
Marks[4]=54
54>34 t
89 56 54 23 34
Iteration 4:
1=3
Marks[3]=23 j=4 marks[4]=34
34>23 t
89 56 54 34 23
'''