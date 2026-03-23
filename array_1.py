# import array as arr;

from array import *

# array  = arr.array('i',[1,2,3,4,-2])
# print(array)

# array.reverse()

# print(array)

# print(array[0])

# print(array.buffer_info())


# looping on ARRAY 
# for el in array:
#     print(el)

# print('--------------')

# for i in range(len(array)):
#     print(array[i])


# array on charachters

# arr = arr.array('u',['a','e','i','o','u'])

# print(arr)

# for el in arr:
#     print(el)



# copying one array in another

# arr1  = arr.array('i',[1,2,3,4,5])
# print(arr1)

# newArr = arr.array(arr1.typecode,(val for val in arr1))

# print(newArr)



# newArr = arr.array(arr1.typecode,(a*a for a in arr1))

# print(newArr)


# using while loop

# arr1  = arr.array('i',[1,2,3,4,5])
# i = 0

# while i < len(arr1):
#     print(arr1[i])
#     i += 1



# Q1
# code to sort array in asc in order

# arr1  = arr.array('i',[5,7,9,2,3])

# lstArr = arr1.tolist()

# srtArr = lstArr.sort()

# print(lstArr)


# # using for loop
# a = arr.array('i', [10,5,15,4,6,20,9])

# for i in range(0,len(a)):
#     for j in range(i + 1,len(a)):
#         if a[i] > a[j]:
#             temp = a[i]
#             a[i] = a[j]
#             a[j] = temp
# print(a)


# find factorial 
# num = int(input('enter number:'))

# fact = 1

# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#     for i in range(1,num + 1):
#         fact = fact * i 
#     print("The factorial of",num,"is",fact)



# INSERT ELEMNT in array 
# my_array = arr.array('i', [1, 2, 3, 4]) 

# my_array.insert(2, 5)

# print(my_array)


# array value form user in python(creating array when valuee coming from user)\
arr = array('i',[])

l = int(input('enter length of array:'))

for i in range(l):
    usrVal = int(input('enter element  array:'))
    # arr.insert(i,usrVal)
    arr.append(usrVal)
    i += 1

print(arr)

# searching in array
# manually
val = int(input('enter value that u want to search in array:'))


ind = 0
for v in arr:
    if v == val:
        print('found:', v, 'at pos:', ind)
        break
    ind += 1
    
# using index func
print(arr.index(val))