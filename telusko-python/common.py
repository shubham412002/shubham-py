name  = 'you tube'
# strings are immutable so we  cant change them
nName = 'my' + name[3:]
print(nName)

# string slicing
name = 'Shubham Patankar'
nameSlice = name[0:7]  # 0 to 6 index
print(nameSlice)

print(len(name))

# list 
nums = [23,56,7,90,67]
print(nums)
print(len(nums))

# list are mutable so we can change them
nums[2] = 45

# list slicing
print(nums[1:4])  # 1 to 3 index

# list can have diffrent data types
mixList = ['Shubh',24,1.9]

nms= ['Shubham', 'Tony', 'Steve', 'Natasha']
rollNo = [23, 45, 67, 89]
details = [nms, rollNo]

print(details)

# list methods
# adding
nums.append(100)
print(nums)

nums.insert(2, 78)
print(nums)

num1 = [4,6,4,35,32]
nums.extend(num1)
print(nums)

# removing
nums.remove(67) #by value
print(nums)

rollNo.remove(8)#raise an error if x is not there in list

nums.pop() #by index if not given removes last element
print(nums)
nums.pop(2)
print(nums)

# nums.clear() #removes all elements
# print(nums)

# delete in range
del nums[1:4]
print(nums)

# inbuilt function 
print(sum(nums))
print(min(nums))
print(max(nums))

# sort
# nums.sort()
# print(nums)

# reverse
nums.reverse()
print(nums)

print(nums.count(4))

# tuple
# tuples are immutable collections like list
tp = (23,45,67,89,45)
print(tp)

mixedTup = (12,'Shubh','Pappa')
print(mixedTup)

# tp[2] = 90 # this will give error

# indexing and slicing
print(tp[1])
print(tp[0:3])

# tuple methods
print(tp.count(45))
print(tp.index(67))
print(tp.__add__((100,200)))  # concatenation


# Sets
# Set is a collection of unique elements which is made to make opertion faster 

st = {23, 45, 67, 89, 23}  # duplicates are not allowed
print(st)

# indexing and slicing not allowed in sets because it uses hashing technique for fetching ele
# print(st[0])  # this will give error

# set methods
st.add(100)  # adding an element
print(st)
st.remove(45)  # removing an element
print(st)
# st.remove(78) # this will give error if element not present
st.discard(67)  # removing an element, if not present it will not give error
print(st)
st.pop()  # removes a random element
print(st)
# st.clear()  # removes all elements
print(st)
# del st  # deletes the set completely


# more on variables
a = 10
b = 20
print(id(a))  # id gives the memory address of the variable
print(id(b))

c = a  # c is now pointing to the same memory location as a
print(id(c))

print('------------------ Data types in Python -------------------')
# datatypes
# None
# Numeric - int,float,complex,Boolean(True,False/ 1/0)
# below are sequence types 
# list
# tuple
# set
# string
# dictionary
# range

no = None
print(no)

a = 10        # int
b = 23.45     # float
c = 3 + 4j    # complex
d = True      # Boolean

# type coversion 
v = 3.6
d =  int(v)  # float to int
print(d)

x = 7
f = float(x)  # int to float
print(f)

a = 6
b = 5
comp = complex(2,4)
print(comp)

# Boolean
t = True
f = False
print(type(t))
print(bool(1))  # True
print(bool(0))  # False

print(bool('Hello'))  # True
print(bool(''))       # False

print(bool([1,2,3]))  # True
print(bool([]))       # False

print(int(True))   # 1
print(int(False))  # 0

#sequence types 
# list
lst = [1,2,3,4,5]
print(type(lst))  # <class 'list'>
# tuple
t = (3,65,6,899,78)
print(type(t))
# Set
s = {3,56,78,78,58,9}
print(type(s))  # <class 'set'>

# string
str = 'Shubh'
print(type(str))

r = range(1,8)  # 1 to 7
print(r)
print(list(range(1,8)))
print(type(r))  # <class 'range'>

# odd number list using range
odd = list(range(1,20,2))  # start, end, step
print(odd)  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]


# Dictionary
# key-value pairs key must be unique
dt = {'name':'Shubham', 'age':24, 'city':'Pune'}
print(dt)
print(type(dt))  # <class 'dict'>

print(dt['name'])  # accessing value using key
u_name = dt.get('name')  # accessing value using get method
print(u_name)

keys = dt.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

values = dt.values()
print(values)  # dict_values(['Shubham', 24, 'Pune'])

items = dt.items()
print(items)  # dict_items([('name', 'Shubham'), ('age', 24), ('city', 'Pune')])

dt['age'] = 25  # updating value
print(dt)

dt.update({'city':'Mumbai'})  # updating value
dt.update({'country':'India'})  # adding new key-value pair
print(dt)


print('------------------ Operators in Python -------------------')
# -------------------------operators in python
# arithmetic operators
a = 10
b = 3
print(a + b)  # addition
print(a - b)  # subtraction 
print(a * b)  # multiplication
print(a / b)  # division
print(a // b) # floor division
print(a % b)  # modulus
print(a ** b) # exponentiation

# assignment operators
x = 5
x += 3  # x = x + 3
x -= 2  # x = x - 2
x *= 4  # x = x * 4
x /= 2  # x = x / 2
x %= 3  # x = x % 3
print(x)

# comparison operators
a = 10
b = 20

print(a == b)  # equal to
print(a != b)  # not equal to
print(a > b)   # greater than
print(a < b)   # less than
print(a >= b)  # greater than or equal to
print(a <= b)  # less than or equal to

# logical operators
x = True
y = False
print(x and y)  # logical AND
print(x or y)   # logical OR
print(not x)    # logical NOT

# membership operators
lst = [1,2,3,4,5]
print(3 in lst)    # True
print(6 not in lst)  # True

# identity operators
a = 10
b = 10
print(a is b)      # True
print(a is not b)  # False

# unary operators]
a = 5
print(+a)  # unary plus
print(-a)  # unary minus    


# swap to variaables in python
a = 3
b = 6

a,b = b,a

# temp = a
# a = b
# b = temp

# a = a + b 
# b = a- b 
# a = a-b

print(a)
print(b)

print('------------------ Math module -------------------')
# Math module
from math import *

print(sqrt(16))  # square root
print(pow(2,3))  # power

print(floor(4.7))  # floor value
print(ceil(4.3))   # ceiling value

print(round(4.8))  # round value
print(round(4.4))  # round value

print(factorial(5))  # factorial
print(gcd(12,15))    # greatest common divisor
print(lcm(12,15))    # least common multiple
print(pi)            # value of pi
print(e)             # value of e   
print(sin(pi/2))    # sine value
print(cos(0))       # cosine value
print(tan(pi/4))    # tangent value
print(log(100,10))  # logarithm base 10 of 100
print(log2(8))      # logarithm base 2 of 8


print('------------------ Input and Output in Python -------------------')
# Input and Output in Python
# input function
# name = input("Enter your name: ")
# print("Hello, " + name + "!")
# age = int(input("Enter your age: "))
# print(f"You are {age} years old.")

# take char from user
# char = input("Enter a character: ")[0]
# print(f"You entered: {char}")

# evaluate expression
# expr = input("Enter a mathematical expression: ")
# result = eval(expr)
# print(f"The result is: {result}")

# import sys
# print(sys.argv[0])
# print(sys.argv[1])
# print(sys.argv[2])

print('------------------ if-else if-elif-else in Python -------------------')
# check number is odd or even also greater than 5 or not
num = 2

if num %2 == 0:
    print(f"{num} is even")
    if num > 5:
        print(f"{num} is greater than 5")
    else:
        print(f"{num} is not greater than 5")
else:
    print(f"{num} is odd")

print('done')


# elif ladder
marks = 85
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Grade D")


# check number is positive, negative or zero
number = -65
if number > 0:
    print(f"{number} is positive")
elif number < 0:
    print(f"{number} is negative")
else:
    print(f"{number} is zero")


# out of three numbers find the greatest number
a = 45
b = 78
c = 23
   
if a >= b and a >= c:
    print(f"{a} is the greatest number")
elif b >= a and b >= c:
    print(f"{b} is the greatest number")
else:
    print(f"{c} is the greatest number")



print('--------------while loop in Python -------------------')

i = 0
while(i < 5):
    print(f"Iteration {i+1}")
    i += 1
print("Done")

# while in reverse manner
i = 5
while(i > 0):
    print(f"Iteration {i}")
    i -= 1
print("Done")


# problem: print
'''
Shubham rocks rocks rocks rocks
Shubham rocks rocks rocks rocks
Shubham rocks rocks rocks rocks
Shubham rocks rocks rocks rocks
Shubham rocks rocks rocks rocks
 '''
i = 5 

while i >= 1:
    print("Shubh ", end='')
    i -= 1 
    j = 1
    while(j <= 4):
        print('rocks ',end='')
        j+=1
    print()


# 
print('--------------for loop in Python -------------------')
lst = ['Shubh',24,'Dev','KT']
for i in lst:
    print(i)

str = 'Shubham'
for i in str:
    print(i)

# numbers from 1 - 10 
for i in range(0,10):
    print(i + 1)

# from 11 to 20 -range start, stop , step
for i in range(11,21,1):
    print(i)


for i in range(11,21,2):
    print(i)

# in reverse order
for i in range(20,1,-1):
    print(i)

#for value divisible by 5 neglect
for i in range(1,21):
    if i % 5 != 0:
        print(i) 


print('------------------Break-Continue-pass---------')
# Break- break and comes  out of loop
# candies eg.
av = 15
x = int(input('How many candies u want?'))
i = 1
while(i <= x):
    if(i > av):
        print(f'last {av} candies was there')
        break
    print(i)
    i += 1
print('bye')

# Continue- skip the current loop execution
# assignment print all numbers from 1-50 skip values divisible by 3 OR 5
for i in range(1,51):
    if(i % 3 == 0 or i % 5 == 0):
        continue
    print(i)

# Pass- pass the condition block in python we cant keep any copndition block empty cause of indentation so use pass
for i in range(1,51):
    if(i % 2 != 0):
        pass
    else:
        print(i)




print('---------------Break-continue-pass in practice------')
# stop the iteration when i is 3
for i in range(1,6):
    if(i ==3):
        break
    print(f'hello {i}')

# skip the iteration when i is 3
for i in range(1,6):
    if(i ==3):
        continue
    print(f'hello {i}')
    
# its not fixed yet what to put in the iteration when i is 3 use pass means in future u will decide 
for i in range(1,6):
    if(i ==3):
        pass

def fun():
    pass

fun()



print('--------------patterns-----------------')
'''
# # # #
# # # #
# # # #
# # # #
'''
for i in range(4):
    for j in range(4):
        print('# ',end='')
    print()

'''
# 
# # 
# # # 
# # # #
'''
for i in range(4):
    # print(i)
    for j in range(i+1):
        # print(j)
        print('# ',end='')
    print()


'''
# # # #
# # #
# # 
#
'''
for i in range(4,0,-1):
    # print(i)
    for j in range(i):
        # print(j)
        print('# ',end='')
    # i-=1
    print()

# OR
n = 4
for i in range(n):
    for j in range(n-i):
        print('# ',end='')
    print()


# assignent
'''
1 
2 2
3 3 3
4 4 4 4
'''
for i in range(4):
    # print(i)
    for j in range(i+1):
        # print(j)
        print(f'{i + 1} ',end='')
    print()


'''
1 2 3 4
2 3 4 
3 4 
4
'''

for i in range(4):
    # print(i)
    for j in range(i + 1,5):
        print(f'{j} ',end='')
    print()



'''
A P Q R
A B Q R
A B C R
A B C D
'''

import string

letters = string.ascii_uppercase

for i in range(4):
    for j in range(4):
        if j < i:
            print(letters[j], end=' ')
        elif j == i:
            print(letters[i], end=' ')
        else:
            print(letters[j + 14], end=' ')
    print()



print('------------for-else --------------')
nolist = [23,56,67,1,68,9]
for i in nolist:
    if(i % 5 == 0):
        print(i)
        break #if want only first occurrence
    # else:
    # print('number not found') # this will run for each iteration 
else:
    print('number not found')

# but if u are getting data from diffrent souce and that dont have number which satisfies current situation on that case u can use for-else 

# find if number is prime or not
num = int(input("Enter a number: "))

if num < 2:
    print("Not prime")
else:
    for i in range(2, num):
        if num % i == 0:
            print("Not prime")
            break
    else:
        print("Prime")

print('---------------array-------------------')
import array as arr

vals = arr.array('i',[3,4,5,6,7])

# vals2 = arr.array('i',[3,4,8.5,6,7]) #rais error cause araay type is defined as int and have value float

# vals1 = arr.array('I',[3,-4,5,6,7]) #unsigned int still passing negative val

print(vals)

print(vals.buffer_info()) #returns tuple with memory address and size
print(vals.typecode) #returns type of array 

vals.append(9)
print(vals)

vals.insert(4,1)
print(vals)

vals.reverse()
print(vals)

print(len(vals)) 

# for i in vals:
#     print(i)

# while loop
i = 0

while i < len(vals):
    print(vals[i])
    i += 1

# crating array from exting or other data
newArr = arr.array(vals.typecode, (a for a in vals))
print(newArr)


# taking array values from user and serch it in array 
import array as arr
userArr = arr.array('i',[])

l = int(input('enter length of array:'))

for i in range(l):
    num = int(input(f'enter {i} val-'))
    userArr.append(num)

# finding ele in array 
fNum = int(input('enter ele to find in array:'))

# manual way
# pos = 0
# for e in range(len(userArr)):
#     if  userArr[e] == fNum:
#         pos = e

ind = 0
for e in userArr:
    if  e == fNum:
        print(ind)
        break
    ind +=1
print(f'ele u seached for found at index: {ind}')

# by inbbuilt method
# pos = 0
# for e in range(len(userArr)):
#     if  userArr.index(fNum):
#         pos =  userArr.index(fNum)

print(userArr)
print(f'ele u seached for found at index: {pos}')

# Q1 sort array in asecending order
import array as arr

vals = arr.array('i',[10,2,6,1,8,9,3])

for i in range(len(vals)):
      for j in range(i + 1,len(vals)):
          if vals[i] > vals[j]:
              temp = vals[i]
              vals[i] = vals[j]
              vals[j]  = temp
print(vals)


import array as arr

vals = arr.array('i', [10, 2, 6, 1, 8, 9, 3])

for i in range(len(vals)):
    for j in range(i + 1, len(vals)):
        if vals[i] > vals[j]:
            vals[i], vals[j] = vals[j], vals[i]

print(vals)


# code to find factrial 
n = int(input("Enter number: "))

fact = 1
for i in range(1, n + 1):
    fact = fact * i

print("Factorial =", fact)


def factorial(n):
    if n < 0:
        print("Factorial not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))


print('-------multi dimensioanl arrays with numpy------')
import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)
print(arr.mean())

# ways of creating arrays in numpy
# array()
# linspace()
# logspace()
# arange()
# zeroes()
# ones()


from numpy import *

arr = array([1,2,3,5])
print(arr)
print(arr.dtype)

arr1 = array([1,3,5,8,6.5]) 
print(arr1)
print(arr1.dtype)

# implicite type 
arr3 = array([1,2,3,4,5.5],int)
print(arr3)
print(arr3.dtype)

arr4 = array([1,2,3,4,5.5],float)
print(arr4)
print(arr4.dtype)

# linspace
arr5 = linspace(0,1)
print(arr5)
# start stop parts 
arr5 = linspace(0,15,30)
print(arr5)

# logspace
arr = logspace(1,40,5)
print(arr)
# create array in range log 10 raise 1 to 10 raise 40 with gap of 5 ele

# divides parts in diffrent spaces based on log 

# arange
# start stop step
arr = arange(1,20,2)
print(arr)

# zeroes - create array with defined size with all 0
arr = zeros(5)
print(arr)

# ones -  create array with defined size with all 1
arr = ones(5)
print(arr)

# by default it will give u float type if u want int 
arr = ones(5,int)
print(arr)



print('------------array operations and deep and shallow copy copying an array using existing array----------')

# assignment take sample array and create another array by adding 5 in each elemnt of array
import array as arr
arr1 = arr.array('i',[4,5,6,7])
newArr = arr.array('i',[])

for i in arr1:
    c = i + 5
    newArr.append(c)

print(newArr)


# same using numpy is 
import numpy as np

arr2 = np.array([1,2,3,4,5])

newArr = arr2 + 5

print(newArr)

# vectoirized operations 
# addition of elements of 2 arrays
# here u need to have same lengths of 2 arrays
arr1 = np.array([1,2,3,4])
arr2 = np.array([5,6,7,8])
arr3 = arr1 + arr2
print(arr3)

print(np.sin(arr1))
print(np.cos(arr1))
print(np.log(arr1))
print(np.sum(arr1))
print(np.min(arr1))
print(np.max(arr1))
print(np.sort(arr1))
print(np.unique(arr1))

# to create single array from two arrays
nArray = np.concatenate([arr1,arr2])
print(nArray)

# copying one array to another
arr1 =  np.array([3,4,6,7])
arr2 = arr1

print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# deep and shallow copy 
# shallow - creates objects which will refer to diffrent memory location means changing value of anh object will reflect in both. Created using .view()
import numpy as np
arr1 =  np.array([3,4,6,7])
arr2 = arr1.view()
arr2[1] = 5
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))

# deep -creates standalone objects in memory which are not interlinked with each others created using .copy()

arr1 =  np.array([3,4,6,7])
arr2 = arr1.copy()
arr2[1] = 5
print(arr1)
print(arr2)
print(id(arr1))
print(id(arr2))




print('----------matrix in python--------------')
from numpy import *
arr1 = array(
    [
        [1,2,3],
        [4,5,6]
    ]
)

print(arr1)
print(arr1.dtype)
print(arr1.ndim) #dimension
print(arr1.shape) #rows and col count
print(arr1.size) #total count

# create new single dimensional array from multi 
arr2 = arr1.flatten()


# now from single to multi
