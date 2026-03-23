# list -    used to store set of  values of any data types 
# list are mutable unlike strigs which are immutable

# for eg
lst = ['Apple','Aakash',2,7.7,True]
print(lst)

# 🔹 Common List Operations
# 1 Accessing ele by indexes
print(lst[0])
print(lst[1])


# 2. Slicing
print(lst[2:4])


# 3. Modifying Elements
lst[0] = 'Orange'
print(lst)

# Adding ele
# append -Adds to end	
lst.append('Angad')
print(lst)

# insert-Inserts at index i
lst.insert(4,'Bravo')
print(lst)

# extend-used to join 2 lists
lst1 = [2,5,6]
lst.extend(lst1);
print(lst)

# \\Removal
# remove(x)	Removes first occurrence of x
lst.remove(2)
print(lst)

# pop(i)	Removes and returns item at i if not i then removes last ele
lst.pop()
print(lst)

lst.pop(2)
print(lst)

# clear()	Removes all items	
# lst.clear()
# print(lst)


# list methods
# .in case of strngs they were retruning new string each time after running method on it here as lists are mutable they do changes in original lst
# 1.len
print(len(lst))

# 2.in	Check membership
print('Bravo' in lst)
print('bravo' in lst)


# my_list.index(x)	First index of x
res = lst.index('Angad')
print(res)

# my_list.count(x)	Count occurrences of x
lst3 = [3,5,7,9,4,3,2,3]
print(lst3.count(3))
print(lst3.count(2))

# my_list.sort()	Sort in-place
lst3.sort()
print(lst3)

# sorted(my_list)	Returns sorted copy
lst4= [3,4,6,7,9,2]
srtLst4 = sorted(lst4)
print(srtLst4)

# my_list.reverse()	Reverses in-place
lst4.reverse()
print(lst4)

# 7. Loop Through List
for item in lst:
    print(item)

# or with index
for i, val in enumerate(lst):
    print(i, val)

# 8. List Comprehension

squares = [x*x for x in range(5)]  # [0, 1, 4, 9, 16]
evens = [x for x in range(10) if x % 2 == 0]

print(squares)
print(evens)




# ///Tuples/// ()
# same as list but its immutable

# A tuple is a collection of ordered, immutable (unchangeable) elements.
# It’s like a list, but you can’t modify the elements once it's created.

tup = ('Shubh',4,2002,4.7,'Rani',5,4)
print(type(tup))

# common operations
# indexing
print(tup[4])

# slicing
print(tup[1:4])

# to make empty tuple
tup1 = ()
print(type(tup1))

# to make tuple with single ele
tup2 = (1)
print(type(tup2)) #this will not cerate 

tup3 = (1,)
print(type(tup3)) #this will  cerate 

# 🔹 Useful Tuple Functions
# len(t)
print(len(tup))

# index(x) returns first index of x in tuple
ind = tup.index(2002)
print(ind)

# ind1 = tup.index(2003)
# print(ind)#will give error

#  count(x) returns the count of X
cnt = tup.count(4)
print(cnt)

# membership- in
print(4 in tup)


# 🔹 Tuple Unpacking
t = (1, 2, 3)
a, b, c = t
print(a, b, c)  # 1 2 3

# list unpacking is also there
lst101 = [1, 2, 3]
h,i,j = lst101
print(h,i,j)  # 1 2 3

# Can also ignore values with _
# a, _, c = (1, 2, 3)


# 🔹 When to Use Tuples?
# When data should not be changed

# As dictionary keys

# To return multiple values from a function

def getPoints():
    return (3,5)

x,y = getPoints()

print(x,y)

# other tuple operations
# concatenation - to join two  tuples 
t1 = (2,4,5)
t2 = (5,7,5)
print(t1 + t2)

# repetations- * 
repeated = t1 * 3
print(repeated)

# membership - in
print(3 in t1)

# len
print(len(t2))

# min , max
print(min(t1))
print(max(t1))

# slicing- 
t5 = (5,6,7,8,5,7,3,2)
print(t5[3:7])
print(t5)



# practice set 
# 1. Write a program to store seven fruits in a list entered by the user.
# fruits = []

# for i in range(7):
#     frt = input(f'Enter fruit name {i + 1}: ')
#     fruits.append(frt)

# print(fruits)


# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
# marks = []

# for i in range(6):
#     frt = input(f'Enter marks of student{i + 1}: ')
#     marks.append(frt)

# marks.sort()
# print(marks)

# 3. Check that a tuple type cannot be changed in python.
# t7 = (5,7,9,8,9)
# t7[0]= 8


# 4. Write a program to sum a list with 4 numbers.
total = 0

lst6 = [7,8,9,6]

# sum() 
# print(sum(lst6))

for i in range(4):
    total = total + lst6[i] 

print(total)

# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))