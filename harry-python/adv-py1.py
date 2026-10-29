# walrus operator
# in py 3.8 introduced new operator 
# allows u to assign values to varibles as part of expression  its used as := ; called as assignment expression.

if(n := len([1,2,3,4]) > 3):
    print(f'list is too long ({n} elements expected <=3)')

# so n is assinged value of length of list and used for comparison expression as well



# Types definition in python
# type hints are added :  for defining types and return types in python

# variable type hint
age: int = 24

name:str = "Shubham"

# function type hint
def greeting(name: str) -> str:
    return f"Hi {name}"

res = greeting("Shubh")
print(res)

def sum(a:int , b:int) -> int:
    return a + b

res  = sum(2,3)
print(res)



# Types defintion in python
from typing import List, Tuple,Dict, Union

numbers:List[str] = [1,2,3,4,5]
numChars:List[int,str] = [1,'shubh',45]

print(numbers)
print(numChars)

# tuple with str and int
person:Tuple[str,int] = ('Alice',30)


# dict with str keys and int value
scores:Dict[str,int] = {'Shubh':90, 'Raj':85}
print(scores)

# int keys and string value
stdRno:Dict[int,str] = {1:"shubh", 25:'Rani'}
print(stdRno)

# Union type
identifier:Union[str,int] =  'ID1234'

identifier = 12345 #this is also valid

# here while normal execution it will not break any code even for wrong assignmenst and type checks if u use any 3rd party typechecker library it can give u error lik mypyYour code:

# from typing import Dict

# stdRno: Dict[str, int] = {1: "shubh", 2.5: "Rani"}

# print(stdRno)

# runs successfully even though: float used 

# Dict[str, int] means:
# Keys should be str
# Values should be int

# But you're providing:

# {
#     1: "shubh",      # int key, str value
#     2.5: "Rani"      # float key, str value
# }
# Why doesn't Python throw an error?

# Because type hints are mainly for:

# IDEs (VS Code, PyCharm)
# Static type checkers like mypy
# Better documentation and code readability

# Python itself ignores them during execution.

# Example:

# name: str = 100

# print(name)

# Output:

# 100

# No error is raised.

# If you use a type checker

# Create a file:

# from typing import Dict

# stdRno: Dict[str, int] = {1: "shubh", 2.5: "Rani"}

# Run:

# mypy filename.py

# You'll get errors similar to:

# error: Dict entry 0 has incompatible type "int": "str"
# error: Dict entry 1 has incompatible type "float": "str"



# Match case 
# match case it is similar to switch statement in found in other languages
# this invloves matching variables against several cases using  case keyword

def http_status(status):
    match status:
        case 200:
            return 'OK'

        case 404:
            return 'Not Found'
        
        case 500:
            return 'Internal server error'
        
        case _:
            return 'Unknown status'
# _ is default case keep always last to this one

print(http_status(200))
print(http_status(500))
print(http_status(405))

# basic syntax
day= 2

match day:
    case 1:
        print('Monday')
    
    case 2:
        print('Tuesday')
    
    case 3:
        print('Wednesday')
    
    case _:
        print('Invalid day')


# Matching Strings
command = "start"

match command:
    case "start":
        print("Starting...")
    case "stop":
        print("Stopping...")
    case _:
        print("Unknown command")


# Matching Tuples
point = (0, 5)

match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y-axis at {y}")
    case (x, 0):
        print(f"X-axis at {x}")
    case (x, y):
        print(f"Point ({x}, {y})")


# Matching Lists
data = [1, 2, 3]

match data:
    case [1, 2, 3]:
        print("Exact match")
    case [1, *rest]:
        print("Starts with 1", rest)
    case _:
        print("No match")

# Using Conditions (Guards)
age = 20

match age:
    case x if x >= 18:
        print("Adult")
    case _:
        print("Minor")

# Matching Dictionaries
person = {"name": "Shubh", "age": 25}

match person:
    case {"name": name, "age": age}:
        print(f"{name} is {age} years old")
    case _:
        print("Invalid data")



# dictionary merger and update opertaor
# 1. dictionary merger operator

dict1 = {"name": "Shubh", "age": 25}
dict2 = {"city": "Kolhapur", "country": "India"}

res = dict1 | dict2

print(res)


# if values overlaps right one will always it will keep latest dict value
dict1 = {"name": "Shubh", "age": 25}
dict2 = {"age": 30,'country': "India"}

res = dict1 | dict2
print(res)



# 2.Dictionary update operator
dict1 = {"name": "Shubh", "age": 25}
dict2 = {"city": "Kolhapur"}

dict1 |= dict2

print(dict1)

# same as 
dict1.update(dict2)

# differance between | and |=

d1= {'x':3}
d2 = {'y': 4}

rd = d1 | d2

print(d1) #unchanged 
print(d2) #unchanged 
print(rd) #merged
 
# vs 
d1= {'x':3}
d2 = {'y': 4}

d1 |= d2
print(d2) #unchanged 
print(d1) #upadted 

# d1 modified directly 


# u can use multiple context manager in single  "with"
with (
    open('shubham-py/harry-python/poem.txt') as f1,
    open('shubham-py/harry-python/log.txt') as f2
):
    data1 = f1.read();
    data2 = f2.read()
    print(data1)
    print(data2)



# here we are handling 2 files at same time

# exception handling in python
# When u dont want to abruptly broke our program excution without having error in further code block use exception handlingn if user did sowmthing wrong the execution will stop there but in functional app this is not good 

# for ex.
# a = int(input('enter a number:'))
# print(a)

# print('Thanks')

# here it will break flow in first line if user enters wrong int and also next code excution will stop

# but with exception handlign
try:
    a = int(input('enter a number:'))
    print(a)

except Exception as e:
    print(e)

print('Thanks')


# handling multiple exception
try:
    a = int(input('enter a number:'))
    print(a)


    b = int(input('enter num for division'))
    print(b)

    res = a/b
    print(res)

except ValueError as v:
    print('Heyy value error')
    print(v)

except ZeroDivisionError as z:
    print('ZDE')
    print(z)

except Exception as e:
    print(e)

print('Thanks')




# Raising exception
# Sometimes its required to raise error also for Devs use case 
a = int(input("enter a number:"))
b = int(input("enter another number:"))

if(b == 0) :
    raise ZeroDivisionError('Hey our program is not meant to divide number by 0')
else :
    print(f'Division of a/b is {a/b}' )


# Try with else and try with finally
try:
    a = int(input('enter a number:'))
    print(a)

except Exception as e:
    print(e)

else:
    print('Inside else')
    print('Thanks')

# else blovk only runs when try block successfully runs
# sometimes we want to do something after try successfully runs in that scae use try-expect-else

# try:
#     code..

# except:
#     code..

# else:
#     code..


# this only runs when try ran successfully 


# try with finally
# Python offers finally block which ensures excution of piece of code irrespective of the execution was valid or not 

try:
    a = int(input('enter a number:'))
    print(a)

except Exception as e:
    print(e)

finally:
    print('Inside finally')


# see when we handle exception aftr that anything task u want to run u can do but why finally requires is when function or block have return at end it will not run nomal code but when its inside finally 

def main():
    try:
        a = int(input('enter a number:'))
        print(a)
        return 

    except Exception as e:
        print(e)
        return

    print('Inside finally')

main()

# in above case it will not run end block

def main():
    try:
        a = int(input('enter a number:'))
        print(a)
        return 

    except Exception as e:
        print(e)
        return
    
    finally:
        print('Inside finally')
        
main()
# in this case even whether return is there finally runs for sure 
