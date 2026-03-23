# import whole lib.
# import math as m

# print(m.sqrt(25))


# print(m.floor(1.8))

# print(m.ceil(2.5))

# print(m.pow(2,5))

# print(m.pi)

# print(m.e)






# import only specific func from lib.
from math import sqrt,pow

print(pow(3,2))

print(sqrt(9))

# help('math')


# swappin two variables
num1 = 9
num2 = 3

num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2

print(num1)
print(num2)


num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print(num1)
print(num2)

num1,num2 = num2,num1

print(num1)
print(num2)





# user input || commmand line input 

# x = int(input('enter num 1:'))

# y = int(input('enter num 2:'))

# res = x + y

# print(res)




# program to accept char from user
# ch = input('enter a char:')
# print(ch[0])

# or
# ch = input('enter a char:')[0]
# print(ch)




# if else 

# given number is even or odd
d = 2

if d % 2 == 0:
    print('even')

    if d > 5 :
        print('great')
    else:
        print('small')
else:
    print('odd')




# elif use
a = 2

if a == 1:
    print('one')
elif a ==2:
    print('two')    
elif a == 3:
    print('three')
elif a ==4:
    print('four')
else:
    print('try again')


#---while loop----
i = 1
while i <= 5:
    print('Shubh',i)
    i += 1


# in reverse order
i = 5
while i >= 1:
    print('Shubh',i)
    i -= 1
 

#nested while loop
print('nested while loop')
i = 1


while i <= 5:
    print('Shubh ',end='')
    j= 1
    while j <= 4:
        print('rocks ',end='')
        j += 1
    i += 1
    print()




# for loop 

arr = ['Shubh',22,'Dev']

for i in arr:
    print('el-',i)


str = "Shubh"

for i in str:
    print(i)


# range func
for i in range(10):
    print('el',i)

# start stop iteration
for i in range(11,21,1):
    print('el',i)


for i in range(11,21,2):
    print('el',i)


for i in range(40,0,-5):
    print('elr',i)
