print('-------Array in python -----')
# import array as arr
from array import *
# signed int allows to have negative integer
vals = array('i',[3,4,-6,8,9])
print(vals)
# vals = array('I',[3,4,-6,8,9]) #this will give error cause its unsigned int
# float array
val1 = array('f',[3.5,6,6.87,9.7])
print(val1)

# indexing in array
print(vals[3])


# loop on array 
for i in vals:
    print(i)

for i in range(len(vals)):
    print(vals[i]) 

# inbuilt methods
print(vals.buffer_info()) #returns tuple with address and size
print(val1.typecode) #return tpe of array

vals.reverse()
print(vals)

vals.append(7)
print(vals)

vals.remove(7)
print(vals)

chars = array('u',['a','e','i','o','u'])
print(chars)

for i in chars:
    print(i)


# creating array from exiting array or its coming from different source then 
arr = array('i',[67,76,34,21,89])

newArr = array(arr.typecode,(a for a in arr))

newSqrArr = array(arr.typecode,(a*a for a in arr))
print(arr)
print(newArr)
print(newSqrArr)


# loop on array using while loop
i = 0 
while(i < len(newArr)):
    print(newArr[i])
    i += 1


# assignment 1
# write code to sort array in ascending order
numArr = array('i',[3,16,27,5,17,8])
numArr.reverse()
print(numArr)

# assignment 2
# find factorial of user entered number