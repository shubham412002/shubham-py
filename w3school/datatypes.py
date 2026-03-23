# Built-in Data Types
# Text Type:	str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:	dict
# Set Types:	set, frozenset
# Boolean Type:	bool
# Binary Types:	bytes, bytearray, memoryview
# None Type:	NoneType


# Getting the Data Type
x = 5
print(type(x))


# to set data type dont need to declare the data type while declaring the variable
x = "Hello World" # str
x = 20 # int

# to set specific data type we can use the following constructor functions
x = str("Hello World") # str
x = int(20) # int



#Numbers
x = 1    # int
y = 2.8  # float scentific numbers are also float like 3e2
z = 1j   # complex


# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))



# Random Number- in Python dont have random() function to generate random number we have to import random module
import random

print("Random no.",random.randrange(1, 10))




# python casting
# int() - constructs an integer number from an integer literal, a float literal (by rounding down to the previous whole number), or a string literal (providing the string represents a whole number)

# float() - constructs a float number from an integer literal, a float literal or a string literal (providing the string represents a float or an integer) 

# string() - constructs a string from a wide variety of data types, including strings, integer literals and float literals

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'





# Strings - strings are immutable in python
# they are always enclosed in single or double quotes


# Quotes Inside Quotes
# u can use quotes insode quoetes until they didnt match with the string quotes

print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# OR
# To put quotes inside the string, use the escape character \:
txt = "We are the so-called \"Vikings\" from the north."
print(txt)



# Multiline Strings
# You can assign a multiline string to a variable by using three quotes u can use 3 single or double quotes

# a = """Lorem ipsum dolor sit amet,
# consectetur adipiscing elit,
# sed do eiusmod tempor incididunt
# ut labore et dolore magna aliqua."""
# print(a)



# String as Arrays we can access letters form string
a = "Hello, World!"
print(a[1])


# Looping Through a String
for x in "banana":
  print(x)
