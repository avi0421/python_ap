# Program to determine grade based on percentage
percentage = float(input('Enter your percentage: '))

# Determine the grade based on the percentage
if percentage >= 90:
    grade = 'A'
elif percentage >= 80:
    grade = 'B'
elif percentage >= 70:
    grade = 'C'
elif percentage >= 60:
    grade = 'D'
elif percentage >= 50:
    grade = 'E'
else:
    grade = 'F'

# Output the grade
print(f'Your grade is: {grade}')
