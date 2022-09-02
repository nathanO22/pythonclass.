# i = 0
# while i < 9:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
# class MyClass:
#   name = "John"

# del MyClass

# print(MyClass)
# x = 4
# if x > 3:
#   print("YES")
# else:
#   print("NO")
# x = "hello"

# try:
#   x > 3
# except NameError:
#   print("You have a variable that is not defined.")
# except TypeError:
#   print("You are comparing values of different type")

# fruits = ["apple", "banana", "cherry"]

# for x in fruits:
#   print(x)

# from datetime import time

# x = time(hour=15 , minute = 51)

# print(x)


# import datetime

# x = datetime.datetime.now()
# print(x)

# x = lambda a, b, c : a + b + c

# print(x(5, 6, 2))
# x = lambda b : b + 10
# x = None

# print(x)
# def myfunc1():
#   x = "John"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())
# def myfunc1():
#   x = "John"
#   def myfunc2():
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())

# print(x(5))

# a = 33
# b = 200

# if b > a:
#   print("accepted")

# if b == a:
#     print("not accepted")

# if b != a:
#     print("not accepted")

# a = 10
# f = a

# a = 29
# print(f)

# for i in range(15) :
#     print(i)
#     if i > 10 :
#         print("greater than 5")


# astr = "Hello Bob"
# #istr = int(AnyStr)
# try :
#     istr = int(astr)
# except :
#     istr = "kucj"
# print('first', istr)

# from tkinter.messagebox import QUESTION


# def name() :
#     print("my first name is Nathaniel")
#     print("my last name is Olowu")

# QUESTION1 = "what is your name?"
# print(QUESTION1)
# name()

# from cgi import MiniFieldStorage
# from sqlite3 import converters
# from unittest.main import MAIN_EXAMPLES


# def function_20(x, y, z):

#     print((x * y) / z)


# function_20(40, 45, 80)

# # BMI calculator
# # name1 = "Jude"
# # height_m1 = 2
# # weight_kg1 = 90

# # name2 = "Natasha"
# # height_m2 = 1.8
# # weight_kg2 = 70

# # name3 = "George"
# # height_m3 = 2.5
# # weight_kg3 = 175


# # def bmi_calculator(name, height_m, weight_kg):
# #     bmi = weight_kg / (height_m ** 2)
# #     print("bmi:")
# #     print(bmi)
# #     if bmi < 23:
# #         return name + " is not overweight"
# #     else:
# #         return name + " is overweight"


# # result1 = bmi_calculator(name1, height_m1, weight_kg1)
# # result2 = bmi_calculator(name2, height_m2, weight_kg2)
# # result3 = bmi_calculator(name3, height_m3, weight_kg3)

# # print(result1)
# # print(result2)
# # print(result3)

# #kilometer converter

# # def change(mile):
# #     print("km:")
# #     return  4 * mile

# # print(change(460))
# # print(change(900))

# print(list(range(1, 100)))
# total1 = 0
# for i in range(1, 100):
#     if i % 3 == 0:
#         print(i)
#     if i % 5 == 0:
#         print(i) 
    
# print(i)    
        
# the_highest = 40
# for numbers in [23, 35, 41, 34, 6**2, (7 * 6), 64, 89, 10**2, (7 * 13), 128, 25**2, 7**3]:
#     if numbers > the_highest:
#         the_highest = numbers
#         print(the_highest, numbers)
# print("after", the_highest)

# poot = 0
# for ante in [6, 55, 76, 60, 47, 44, 49, 40, 41, 80]:
#     poot += 1
#     print(poot, ante)
# print("after", poot)

# def repeat_lyrics():
#     print_lyrics()
#     print_lyrics()
# repeat_lyrics()

# def print_lyrics():
#     print("i am lumberjack, and i'm okay")
#     print("i work all day,and i sleep all night")

# print_lyrics()

# bruce = 200 * 8
# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# print_twice(bruce)

# def print_twice(bruce):
#     print(bruce)
#     print(bruce)
# print_twice('Spam ' * 4)

# def function2():
#     print("open the gates")
#     print("to the bathroom")

# f should a callable
# def do_twice(f):
#     # print(f)
#     print(f)
#     print(f)

# def print_spam():
#     return "Hello:"

# do_twice(print_spam())

# print(print_spam())

# print_spam()
# value = print_spam
# print(value)
# print(print_spam())




# print(print_spam())

# from re import I


# def do_twice(f):
#     f()
#     f()

# def do_four(f):
#     do_twice(f)
#     do_twice(f)

# def print_beam():
#     print('+ - - - -', end=' ')

# def print_post():
#     print('|        ', end=' ')

# def print_beams():
#     do_twice(print_beam)
#     print('+')

# # def print_posts():
# #     do_twice(print_post)
# #     print('|')

# # def print_row():
# #     print_beams()
# #     do_four(print_posts)

# # def print_grid():
# #     do_twice(print_row)
# #     print_beams()

# # print_grid()
    

# # # here is a less-straightforward solution to the
# # # four-by-four grid

# # def one_four_one(f, g, h):
#     f()
#     do_four(g)
#     h()

# def print_plus():
#     print('+', end=' ')

# def print_dash():
#     print('-', end=' ')

# def print_bar():
#     print('|', end=' ')

# def print_space():
#     print(' ', end=' ')

# def print_end():
#     print()

# def nothing():
#     "do nothing"

# def print1beam():
#     one_four_one(nothing, print_dash, print_plus)

# def print1post():
#     one_four_one(nothing, print_space, print_bar)

# def print4beams():
#     one_four_one(print_plus, print1beam, print_end)

# def print4posts():
#     one_four_one(print_bar, print1post, print_end)

# def print_row():
#     one_four_one(nothing, print4posts, print4beams)

# def print_grid():
#     one_four_one(print4beams, print_row, nothing)

# print_grid()
# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)
# b = "Hello, World!"
# print(b[0:5])

# b = "Hello, World!"
# print(b.endswith("i"))

# txt = "Hello, welcome to my world."

# x = txt.endswith("my world." 17, 26)

# print(len(txt))
# print(x)

# import turtle
# bob = turtle.Turtle()

# r = str(2344)
# print(len(r))


# def prime_factor(x:int):
#     # b = []
#     for num in range(1, x+1):
#         if x % num == 0:
#             print(num)

          
# prime_factor(1000)


# a = int(input("input a number: "))
# total = 0
# for i in range(1, a+1, 1):
#     total += i 
# print(total)


# num = 2
# for i in range(1, 13):
#     i *= num
#     print(i)


# numbers = [12, 75, 150, 180, 145, 525, 50]
# for num in numbers:
#     if num % 5 == 0:
#         if num > 499:
#             break
#         elif num > 150:
#             continue
#         print(num)

# list1 = [10, 20, 30, 40, 50]
# for num in sorted(list1, reverse=True):
#     print(num)

import xml.etree.ElementTree as ET
inputs = '''<stuff>
       <users> 
        <user x="2">
            <id>001</id>
            <name>Emmanuel</name>
       </user>
       <user> 
        <user x="7">
            <id>00</id>
            <name>kate</name>
       </user>
       </users>
</stuff>'''

stuff = ET.fromstring(inputs)
lst = stuff.findall("users/user")
print("User count:", len(lst))
for item in lst:
    print("name", item.find("name").text)
    print("Id", item.find("id").text)
    print("attribute", item.get("x"))
    