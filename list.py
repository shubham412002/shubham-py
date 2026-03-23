nums = [12,23,45,56,67,56,66]
print(nums)

print(nums[4])

print(nums[2:4])

print(nums[2:])

print(nums[-1])

print(nums[-5])

names = ['Shubh', 'Ravi','Kiran']

values = [1.23,'Ram',23]

mil = [nums,names]

print(mil)


# lists are mutable
nums.append(34)
print(nums)

# insert ele at specific index
nums.insert(2,89)
print(nums)

# removes first occurence of element provided
nums.remove(56)
print(nums)

# removes ele at specic index if provided otherwise it will remove last ele default
nums.pop(3)
print(nums)

nums.pop()
print(nums)


# delete multiple values at same time
del nums[3:]
print(nums)


# add muiltiple values at same time USE array to define values
nums.extend([11,12,13,14])
print(nums)


print(min(nums))

print(max(nums))

print(sum(nums))

nums.sort()
print(nums)


num1 = [12,56,34,78,54]
num1.sort()
print(num1)




# tuples
# tuples are immutable
 
tup = (21,23,13,67,56)
print(tup[3]) 

# tup[4] = 23




# sets 
# sets always contains unique values and they are same as lists
s = {23,45,47,87,56,70}
print(s)

s = {23,45,47,87,56,70,45,23}
print(s)

# print(s[2]) we cant use indexing cause sequence will not be same always






# dictionaries in python
# stores data in key values pair format

data = {
    1:'Shubh',
    2:'Sunil',
    3:'Dinkar',
    5:'Rani'
} 

print(data[2])
print(data[5])


# print(data[4])


print(data.get(4)) #will return None in case of get methhod if key is not present
print(data.get(5))

# in get we can handle it by passing another argument
print(data.get(4,"Not found"))


#dictionary using lists
keys = ['Shubh',"Navin","Sahil"]
values = ['Python',"JS","PHP"]

dataObj = dict(zip(keys,values))
print(dataObj)


# add new entry in dict

dataObj["Mansa"] = "CS"
print(dataObj)

# remove value from dict
del dataObj['Sahil']
print(dataObj)

# we can nest list and dicts in one another
prog = {
    'JS':'VS code',
    'CS': 'VS',
    'Python':['Pycharm', "Sublime"],
     'Java': {
         'JSE':'NetBeans',
         'JEE':'Eclips'
     }
}

print(prog['JS'])
print(prog['CS'])

print(prog['Python'])
print(prog['Python'][1])

print(prog['Java'])
print(prog['Java']['JSE'])
print(prog['Java']['JEE'])