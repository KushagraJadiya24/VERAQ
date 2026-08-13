
# numbers = [4, 8, 15, 16, 23, 42];
# for num in numbers:
#     if num%2==0:
#         print(num)

# grid = [[1,2],[3,4],[5,6]]
# sum=0
# for i in grid:
#     for j in i:
#         sum= sum + j
# print(j)

#Dictionary
# book = {"title": "Atomic Habits", "author": "James Clear", "pages": 320}
# print(f"{book['title']} by {book['author']}, {book['pages']} pages")

#List
# students = [
#     {"name": "Aditya", "marks": 85},
#     {"name": "Riya", "marks": 92},
#     {"name": "Karan", "marks": 76}
# ]

# for student in students:
#     if student.get("marks")>80:
#         print(student.get("name"))

#Class
# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height= height

#     def area(self):
#         return self.height*self.width
#     def perimeter(self):
#         return 2*(self.height +self.width)

# r1 = Rectangle(5,10)
# print(r1.area())
# print(r1.perimeter())

# #Exception
# def safe_divide(a,b):
#     return a/b

# try:
    
#     safe_divide(10,2)
#     safe_divide(3,0)
# except ZeroDivisionError:
#     print("cannot divide by 0")

# try:
#     risky_code()
# except Exception as e:
#     print("Something went wrong:", e)

# Venv — why it matters

# Every Python project can need different versions of different packages. A virtual environment (venv) creates an isolated, project-specific space so installing packages for one project doesn't mess up another.
# python3 -m venv venv
# venv\Scripts\activate
#import requests