# print a number in the output screen
print(2)
print(3)

# Basic arithmetic operations
print(2+3)
print(2*3)
print(2**3)
print(4**2)
print(45/5)

# print string
print("Hi all")

# lists in python
programming_languages = ["C", "C++", "R", "Python"]

# print the entire list
print(programming_languages)

# print each language in list
for languages in programming_languages:
	print(languages)

# indexes
my_list = [1,2,3,4,5]

# print one second element in list
print(my_list[1])

# print last element in list
print(my_list[4])

# find the length of list
print(len(my_list))

# slicing list
print(my_list[2:4])

# update value in list
my_list[1] = 20

# print the new list
print(my_list)

# store the value
a = 20
b = 30

# add two numbers using function
def addition(x, y):
	return (x+y)

# use the function addition to add two numbers
print(addition(10,20))

# what happens if we try to add two strings
print(addition("Hello,", " How are you"))

# try to add different datatypes
print(addition(10, "Hello"))
