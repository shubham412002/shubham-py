# datatypes / object types

# number - int, float, complex -1234,3.56, 3+4j, 0b111, Decimal, Fraction

# string - 'single quotes', "double quotes"

# list - [10,20,30,40,['one',65]],list(range(10))

# tuple- (10,20,30,40,50), tuple(range(10))

# Dictionary - {'name':'shubh','age':23},dict(name='shubh',age=23)

# set - {10,20,30,40,50}, set(range(10))

# file - open('file.txt','w')

# Boolean - True, False

# None - None

# function, modules, classes

# adnvance: decorators, generators, iterators


# import math # type: ignore
# print(math.sqrt(16))

# import random # type: ignore
# print(random.randint(1,100))
# print(random.random())
# print(random.choice([1,2,3,4,5,6,7,8,9,10]))

# strings
# username = 'shubh'
# print(len(username))


# import pyttsx3
# engine = pyttsx3.init()
# engine.say("Tanmay, bahdwa hai")
# engine.runAndWait()


import os 
dir_path = os.getcwd()
print(dir_path)

content = os.listdir(dir_path)
print(content)


