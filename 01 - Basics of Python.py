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

# find square root
print(49**(1/2))

# alternative way for square root
# importing a library
import math
print(math.sqrt(49))

# list of numbers
print([1,2,3,4,5])

# importing a numeric package called numpy
import numpy

# defining an array
print(numpy.array([1,2,3,4,5]))

# difference between array and list
print(numpy.array([1,2,3,4,5])*5)
print([1,2,3,4,5]*5)

# array operations
print(numpy.array([1,2,3,4,5]) + numpy.array([6,7,8,9,10]))

print(numpy.array([1,2,3,4,5]) / numpy.array([6,7,8,9,10]))

print(numpy.array([1,2,3,4,5]) * numpy.array([6,7,8,9,10]))

# matrix
print(numpy.matrix([[1,2,3,4], [3,4,5,6]]))
print(numpy.matrix('1 2 3 4; 3 4 5 6'))

# matrix operations
m = numpy.matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(m)

# multiply individual elements by 3
print(3*m)

# define m1 as a 3x3 matrix
m1 = numpy.matrix([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# define m2 as a 3x3 matrix
m2 = numpy.matrix([
    [1,4,7],
    [2,5,8],
    [3,6,9]
])

# add matrix m1 and m2 and store it in m3
print(m1+m2)
m3 = m1+ m2
print(m3)

m4 = m1/m2
print(m4)

# matrix multiplication
m5 = m1*m2
print(m5)

# individual element multiplication - use array instead of matrix
m1 = numpy.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

m2 = numpy.array([
    [1,4,7],
    [2,5,8],
    [3,6,9]
])
m6 = m1*m2
print(m6)

# determinant of a matrix
det = numpy.linalg.det(m6)
print(det)
print(numpy.linalg.det(m5))

# inverse of a matrix
inv = numpy.linalg.inv(m6)
print(inv)


# the below line will through an error
# because determinant value is 0 since matrix is singular
#print(numpy.linalg.inv(m5))

################# BASICS OF PYTHON ####################

# There is a need to store the data----
# Each 'data' can be stored and can be used in python

x = 5
y = 10
print(x+y)
print(x/y)
print(x**2)
print(y**2)
print(x**2 + y**2)
print((x**2) + (y**2))

# this bracket saves the value in a list
print([(x**2) + (y**2)])

# the below line will through an error since
# we have not defined z
# variable to be defined appears on the left of = symbol
#x + y = z

z = x + y

print(z)
print(x**2)
print(math.sqrt(z))
print(z+5)

# an array can be stored as a variable

x1 = numpy.array([1,2,3,4,5])
x2 = numpy.array([6,7,8,9,10])

print(5*x1)
print(x1+x2)

za = numpy.array(["male","female"])
print(za)

# suppose if we want to print numbers from 1 - 10
# note the difference
# this is a list
print(list(range(1,11)))
# this is an array
print(numpy.arange(1, 11))

# we can store it in a variable and print the variable
x3 = numpy.arange(1, 11)
print(x3)

#to create sequence [you can save it also]
# numpy.arange(start,stop,step)
print(numpy.arange(1, 11, 1))
print(numpy.arange(1, 10.5, 0.5))
print(numpy.linspace(1, 10, num=10))
print(numpy.linspace(1, 10, num=20))

# to store a sequence as a variable
zb = numpy.arange(1, 10.25, 0.25)
print(zb)

print([10]*4)
print("name"*4)
print(["name"]*4)
print(list(range(1,5))*3)
