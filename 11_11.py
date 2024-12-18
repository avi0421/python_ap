'''
1)A String represents a sequence of characters.
2) It is an immutable data type in most of the programming languages including Java and Python, meaning that once you have 
created a string, you cannot change it. 
3) Python Programming does not have a character data type, a single character is simply a string with a length of 1.

Strings in Python can be created using single quotes or double quotes or even triple quotes.
In this example, we will demonstrate different ways to create a Python String. We will create a string using single quotes), 
double quotes (" "),
and triple double quotes (""" """). The triple quotes can be used to declare multiline strings in Python.
'''
'''
str1 = input("Enter your name: ")
str2 = input("Enter last name: ")
print(str1[0])
print(str1[-1])
# Slicing
print(str1[1:6])
# Concatenation
res = str1 + str2
print("The concatenated string is:", res)
# Repetition (*):
# The operator allows you to repeat a string a specified number of times.
ans = str1 * 4
print("The expected answer is:", ans) '''

'''# Methods related to string
text = "helloWorld"
# Convert to uppercase
text_upper = text.upper()  # Corrected the assignment operator
print("The data in uppercase is", text_upper)
# Convert to lowercase
text_lower = text.lower()  # Corrected the assignment operator
print("The data in lowercase is", text_lower)'''

'''name = "     RajGopal  "
newname = name.strip()
print("The data without space is", newname)
lspace = name.lstrip()
print("The data without leading space is", lspace)
rspace = name.rstrip()  # Corrected variable name
print("The data without trailing space is", rspace)'''

'''#str.replace (old, new): This method replaces all occurrences of the "old" substring 
# with the "new" substring in the string.
sentence = "I like apples, and I like pineapple."
new_sentence = sentence.replace("like", "love")
print(new_sentence)
#" I love apples, and I love pineapple."    '''

'''sentence = "Python programming is fun!"  
words = sentence.split()  # Split the sentence into words
print(words)  # Print the list of words'''

'''name = "Alice"
age = 30
# Using old-style formatting
formatted_str = "My name is %s, and I am %d years old." % (name, age)
print(formatted_str)
# Using a different print method
print("My name is", name, "I am", age, "years old")'''

#WAP to join two strings.
#WAP to compare two different strings

'''str1 = "apple"
str2 = "Apple"

result = str1 == str2  # false
print("The strings are equal:", result)

res1 = str1 != str2  # true
print("The strings are not equal:", res1)  '''