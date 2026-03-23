# immutable version of list
# \it can contain data of multiple type
 
tup = (2,4,7,90,6,332,456,"Jhon","Steven")
print(type(tup))
print(tup)

# to  create tuple with single el
tp = (1,)
print(type(tp))

# methods
print(tup.count(4))#returns first occurrence of el 

print(tup.index(6))

# concatenation
t1 = (1,2,3)
t2 = (5,6,7)
full = t1 + t2
print(full)

# repetition
rep = t1  * 3
print(rep)


# membership
print(1 in t1)


print(len(tup))


# slicing
print(tup[2:5])

# unpacking
p,q,r = t1
print(p,q,r)


# program to ask seven fruits eneted by user and store the in list 
# frtLst = []
# for i in range(0,7):
#     frt = input(f'Eneter {i + 1}:')
#     frtLst.append(frt)

# print(frtLst)


# Write a program to accept marks of 6 students and display them in a sorted manner
# stdLst = []
# for i in range(0,6):
#     mark = int(input(f'Eneter mark of student {i + 1}:'))
#     stdLst.append(mark)


# stdLst.sort()
# print(stdLst)


# 3. Check that a tuple type cannot be changed in python.
# tp4 = (2,4,6,"SP")

# tp4[2] = 4


# 4. Write a program to sum a list with 4 numbers.
# lst1 = [34,56,7,73,67]

# sum = sum(lst1)

# print(sum)


# Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)

cnt = a.count(0)

print(cnt)