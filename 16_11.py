'''#WAP to check whether the number is armstrong number or not #for Example n=153, 371
#sum (3)*3*3+5*5*5+1*1*1
# =27+125+1=153
# 27+343+1=371
n = int(input("Enter a number: "))
num_digits = len(str(n)) 
sum1 = 0
copy1 = n
while copy1 > 0:
    rem = copy1 % 10
    sum1 += rem ** num_digits
    copy1 = copy1 // 10
if sum1 == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")'''

#sets
#A Set in Python programming is an unordered collection data type
#that is iterable and has no duplicate elements. While sets are mutable, meaning you can add or remove elements after their creation

set_a = {5, 8, 67, 3, 6}
print(set_a)

set_b = {6, 9, 5, 6}
print(set_b)

set_c = {7, 9, 78, 4}
print(set_c)

# Set union operation
set_d = set_a.union(set_b)
print("The union of set_a and set_b is:", set_d)

set_e = set_a.union(set_b, set_c)
print("The union of set_a, set_b, and set_c is:", set_e)

#using union operator |
result=set_a|set_b|set_c
print("The union of all is",result)

# Intersection using the '&' operator
result_operator = set_a & set_b
print("The intersection using '&' operator:", result_operator)

# set difference(-)
result_sd=set_a-set_b
print("set difference (-) is",result_sd)

# set difference using difference() method
result_d=set_a.difference(set_b)
print("set difference using difference() is",result_d)

#wap to get symmetric_diff (elements not in both sets )
result_symm=set_a ^ set_b
print("The symmetric diff is",result_symm)

result = set_a.symmetric_difference(set_b)