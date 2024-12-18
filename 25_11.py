'''
class UserInfo:
    def putData(self):
        self.name = input("Enter your Name: ") 
        self.id = int(input("Enter your id: ")) 
        self.salary = float(input("Enter your salary: ")) 
    def display(self):
        print("User Name: ", self.name) 
        print("User Id: ", self.id)
        print("User Salary: ", self.salary)

obj = UserInfo()
obj.putData()
obj.display()


class Student:
    def __init__(self, name, age, grade):
        """
        Initializes the student object.
        """
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        """
        Displays the student's information.
        """
        print(f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}")  # Fixed the closing of the f-string

# Creating objects
student1 = Student("Alice", 14, "9th")
student2 = Student("Bob", 15, "10th")

# Accessing object methods
student1.display_info()
student2.display_info()
'''

# WAP to print bookdata as title,year,author etc with class and object concept
class Book:
    def __init__(self, title, author, year, publisher):
        """
        Initializes the book object.
        """
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher

    def display_info(self):
        """
        Displays the book's information.
        """
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}, Publisher: {self.publisher}")


# Creating objects
book1 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "J.B. Lippincott & Co.")
book2 = Book("1984", "George Orwell", 1949, "Secker & Warburg")

# Accessing object methods
book1.display_info()
book2.display_info()
