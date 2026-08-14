
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


# #json
# import json

# movie = {"title": "Inception", "year": 2010, "genres": ["Sci-Fi", "Thriller"]}

# string= json.dumps(movie,indent=2);
# print(string)
# print(type(string))

# json_string = '{"name": "Aditya", "age": 20}'
# person = json.loads(json_string)

# print(person["name"])     # Aditya
# print(type(person))       # <class 'dict'> — back to a real dict


# http requests 

# import requests

# def get_random_joke():
#     url = "https://official-joke-api.appspot.com/random_joke"
#     try:
#         response = requests.get(url, timeout=5)
#         data = response.json()
#         return data
#     except Exception as e:
#         return f"Request failed: {e}"

# print(get_random_joke())

#  Given prices = {"apple": 50, "banana": 20, "milk": 40, "bread": 35}, print items costing more than 30.
# prices = {"apple": 50, "banana": 20, "milk": 40, "bread": 35}
# for item,price in prices.items():
#     if price> 30:
#         print(item)

# approach 2
# result = {item: price for item, price in prices.items() if price > 30}
# print(result)
# # Given prices from above, find the most expensive item (key and value) without using max() directly on values — loop through it.
# maxPrice=0
# fitem = price.get[]
# for item,price in prices.items():
#     if price>maxPrice:
#         maxPrice = price
#         fitem = item
# print(item,maxPrice)

# Given two dicts, dict1 = {"a": 1, "b": 2} and dict2 = {"b": 3, "c": 4}, merge them into one dict. If a key exists in both, keep dict2's value.
# dict2 = {"b": 3, "c": 4}
# dict1 = {"a": 1, "b": 2}

# merged = {**dict1,**dict2}
# print(merged)


# Given:
# python
# employees = [
#     {"name": "Aditya", "dept": "Engineering", "salary": 55000},
#     {"name": "Riya", "dept": "Marketing", "salary": 48000},
#     {"name": "Karan", "dept": "Engineering", "salary": 60000},
#     {"name": "Neha", "dept": "Sales", "salary": 42000},
# ]

# Print only employees in "Engineering", and separately, calculate the average salary across everyone.

# employees = [
#     {"name": "Aditya", "dept": "Engineering", "salary": 55000},
#     {"name": "Riya", "dept": "Marketing", "salary": 48000},
#     {"name": "Karan", "dept": "Engineering", "salary": 60000},
#     {"name": "Neha", "dept": "Sales", "salary": 42000},
# ]

# sum=0
# count=0
# for items in employees:
#     if items.get("dept") == "Engineering":
#         print(items)
#     sum = sum + items.get("salary")
#     count+=1

# print(sum/count)

# From the same employees list, build a new dictionary that groups names by department, like:
# python
# {"Engineering": ["Aditya", "Karan"], "Marketing": ["Riya"], "Sales": ["Neha"]}
# result = {}

# for engineer in employees:
#     dept = engineer["dept"]
#     name = engineer["name"]

#     if dept not in result:
#         result[dept] = []

#     result[dept].append(name)

# print(result)

#Reverse a List without . reverse()

# nums = [1, 2, 3, 4, 5]

# result = []

# for i in range(len(nums) - 1, -1, -1):
#     result.append(nums[i])

# print(result)