first_name = "Bro"
last_name = "Code"
full_name =first_name +" "+last_name
print("Hello " + full_name)
age = 21
age +=4
print(age)
print(type(age))
print("Your age : " + str(age))
height = 250.5
print("Your height is : " + str(height) + "cm")
print(type(height))
human = True
print("ARE you human?" + str(human))
print(type(human))
name = "Bro"
age = 21
attractive = True
print(name)
print(age)
print(attractive)
name, age , attractive = "Bro", 21, True
print(name, age,attractive)
name = "Bro Code"
print (len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o", "a"))
print(name*3)
x = 1
y = 2.0
z= 3
x = float(x )
y= float(y)
z = float(z)
print(x)
print(y)
print(z*3)
name = input ("What is your name?: ")
age = int(input("How old are you?: "))
height = float(input("How tall are you?: "))
print ("Hello " + name)
print("You are " + str(age)  + "years old")
print("You are " + str(height) + "cm tall")
import math
pi = 3.14
x = 1
y = 2
z = 3
print(round(pi))
print(math.ceil(pi))
print(math.floor(pi))
print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(pi))
# print(max(x,y,z))
# print(min(x,y,z))
# name = "Bro Code"
# last_name = name[4:]
# funky_name = name[::3]
# reversed_name = name [::-1]
# print(last_name)
# print(funky_name)
# print(reversed_name)
#
# """
# 27/06/2023
# Theme: Bro Code (2-part)
# Author: Abdurakhmon Khasanov
# """
#
# # logical operators (and , or , not) = used to check if two or more conditional statement
# temp = int(input("What is the temperature outside"))
# if not(temp >= 0 and temp<=30) :
#     print("The temperature is bad today")
#     print("Stay insiide ")
# elif not(temp<0 or temp>30):
#     print("The temperature is good today")
#     print("Go outside")
#  #while loop = a statement that will execute it's a block of code ,
#  #              as long as it's a condition remains true
# name = ""
# while len(name) ==0:
#     name = input ("Enter your name : ")
#
# print("Hello " + name)
# # for loop = statement that will execute it's block  of code
# #           a limited amount of times
# #           while loop = unlimited
# #           for loop = limited
# for i in range (10) :
#     print(i+1)
# for i in range(50, 100+1, 2 ):
#      print(i)
# for i in "Bro Code " :
#     print (i)
# import time
# for seconds in range (10, 0, -1) :
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")
#
# """
# 30/06/2023
# # Theme: Bro Code(3 part)
# Author: Abdurakhmon Khasanov
# """
#
# rows = int(input("How many rows ?: "))
# columns = int(input("How many columns ? : "))
# symbol = input("Enter a symbol to use : ")
# for i in range (rows):
#     for j in range (columns ):
#          print(symbol , end= "")
#     print()
# rows = int (input("How many rows ? : "))
# columns = int(input("How many columns ?: "))
# symbol = input("Enter a symbol to use : ")
# for i in range (rows) :
#      for j in range (columns ):
#        print(symbol, end = "")
#      print()
# while True:
#     name = input("Enter your name : ")
#     if name != "":
#         break
# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue
#     print(i , end = "")
# for i in range (1, 21):
#     if i == 13:
#         pass
#     else:
#         print(i)
# for i in range (1,21) :
#     if i == 13:
#         pass
#     else:
#         print(i)
# for i in range (1,21):
#     if i ==13:
#          pass
#     else:
#         print(i )
# food = [ "pizza", " hamburger ", "hotdog ", "spaghetti", "pudding"]
# food[0]="sushi"
# # print(food[0])
# food.append("icecream")
# food.pop()
# food.insert(0, "cake ")
# food.sort()
# food.sqrt()
# food.clear()
#  # 2D lists = a list of lists
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
# food = [drinks, dinner, dessert]
# print(food[1][2])
# # tuple = collection which is ordered and unchangeable used to group together related data
# student = ("Bro", 21, "male")
# print(student.count("Bro"))
# print(student. index("male"))
# for x in student :
#     print(x)
# if "Bro " in student:
#     print("Bro is here !")
# # set = collection which is unordered , unindexed . no duplicate values
# utensils = { "fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup"}
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update
# for x in utensils:
#     print(x)
#
# """
# 1/07/2023
# Theme: Bro code (4-part)
# Author: Abdurakhmon Khasanov
# """
#
# # utensils = {"fork", "spoon", "knife"}
# # dishes = {"bowl","plate", "cup", "knife"}
# # utensils.add("napkin")
# # utensils.remove("fork")
# # utensils.clear()
# # dishes.update(utensils)
# # dinner_table = utensils.union(dishes)
# # for x in utensils:
# #     print(x)
# # print(utensils.intersection(dishes))
# capitals = {'USA': 'Washington DC',
#               'India' : 'New Dehli',
#               'China' :  'Beijing',
#               'Russia':   'Moscow' }
# print (capitals["India"])
# print (capitals.get('New Zeland'))
# print(capitals.keys())
# print(capitals.values())
# capitals.update({'Germany': 'Berlin'})
# capitals.pop('China')
# capitals.clear()
# print(capitals)
# name = "bro code:"
# if (name [0].islower() ):
#     name = name.capitalize()
# first_name = name[:3].upper()
# last_name = name [4: ] .lower()
# last_character = name[-1]
# print(first_name)
# print(last_name)
# print(last_character)
# def hello (first_name, last_name):
#     print("hello " + first_name + " "+ last_name)
#     print("Have a nice day! ")
# # my_name = "Bro"
# hello("Bro","Code")
# # hello("Bro")
# # hello("Dude")