x = 7
y = 8

print(x+y)


name = 'Youtube'
print(name + ' Rocks')

# ṣtring indexing and accessing
print(name[0])
print(name[6])
# print(name[8]) #string index out of range error 

print(name[-1])

print(name[0:2])

print(name[1:4])


print(name[1:])

print(name[:5])

# below one will not give u any error 
print(name[3:10])

# u cant change strings as they are immutable
# name[0:3] = "My" #TypeError: 'str' object does not support item assignment


# print my tube using name variable
print('My ' + name[3:])


myname = "Shubh"
print(len(myname))