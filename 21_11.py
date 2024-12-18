#  Q1) write a function to reverse a list without using the buit in reverse function.
def rev_1st(l):
    return l[::-1]
l = [98, 87, 45, 78]
print("The reverse is", rev_1st(l))

# Q2) wap to find 2nd largest element in a list.
l2 = [89,67,54,65,89,78]
remove_dup=(list(set(l2)))
print("The final list is", remove_dup)
sorted_list = sorted(remove_dup)
print("The sorted list is", sorted_list)
print("The 2nd largest element in the list is", sorted_list[-2])

# Q3) WAP to do intersection of two lists.
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = list(set(list1) & set(list2))  # intersection
print("The intersection of the two lists is", intersection)
conjunction = list(set(list1) | set(list2))   # conjunction
print("The conjunction of the two lists is", conjunction)

# Q4: Find Maximum and Minimum from the List
my_list = [89, 67, 54, 65, 89, 78]
maximum = max(my_list)
minimum = min(my_list)
print("Maximum value in the list is:", maximum)
print("Minimum value in the list is:", minimum)

# Q5: Add and Remove Elements from a List
my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("After adding 6:", my_list)
my_list.remove(2)
print("After removing 2:", my_list)

# Q6: Check Whether Two Lists are Palindrome or Not
list1 = [1, 2, 3, 2, 1]
list2 = [4, 5, 6, 5, 4]
palindrome_check1 = list1 == list1[::-1] # Check if list1 is a palindrome
palindrome_check2 = list2 == list2[::-1] # Check if list2 is a palindrome
if palindrome_check1:
    print("list1 is a palindrome")
else:
    print("list1 is not a palindrome")
if palindrome_check2:
    print("list2 is a palindrome")
else:
    print("list2 is not a palindrome")
