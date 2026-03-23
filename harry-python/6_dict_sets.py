# dictionary
# A dictionary is an unordered, mutable collection of key-value pairs.

myDict = {
    'Shubham' : 90,
    'Rohan':89,
    'Vishal':34
}

print(myDict,type(myDict))

# here u cant access any ele with index cause it is unordered
# print(myDict[0])

# here we need to access ele by keys 
print(myDict['Rohan'])

# common dict methods
# items()- returns a list of (key,value) tuples
print(myDict.items())

# keys() - returns list containing dict keys
print(myDict.keys())

# values() - Returns a list of all values
print(myDict.values())

# update() - update dict with new dict means if any key exists it updates its value and if not exits it will add that key value in dict
myDict.update({'Shubham':99,'Harry':89})
print(myDict)

# get(key) - 	Get value by key
val = myDict.get('Shubham')
print(val) 

print(myDict['Shubham']) 

# in above cases both looks same but in get case if key doesn't exits it returns None and second direct access way gives error

# val = myDict.get('Shubham1')
# print(val) #None

# print(myDict['Shubham1'])# returns a Key error  

# A dictionary is an unordered, mutable collection of key-value pairs.

d = {
    "name": "Shubham",
    "age": 23,
    "city": "Mumbai",
    'marks':[78,86,89],
}

print(d)
# Keys must be unique and immutable (strings, numbers, tuples).
# adding duplicate keys will keep latest key value pair in dict
# Values can be of any type.


#ways to create dict 
# Using {}
person = {"name": "Alice", "age": 30,'city' :'Mumbai'}

# using dict() constructor 
person = dict(name='Raj',age=30)

# empty dict 
empty = {}

# 🔹 Accessing Items
print(person['name'])
print(person.get('age'))

print(person.get('Education')) #it will return None 
print(person.get('gender','Not Specified')) #default value it will return Not Specified instead of None

# 🔹 Adding / Updating Items
# add
person['Education'] = "Grad"

# update
person['age'] = 33

print(person)


# 🔹 Removing Items
# pop(key)	-Removes item with key	
person.pop("age")
print(person)

# popitem()	Removes last inserted key-value pair
person.popitem()
print(person)

person['city'] = 'Pune'
print(person)
# del -	Deletes key
del person["city"]

print(person)

# clear()	Removes all items	
# person.clear()


# 🔹 Dictionary Methods
my_dict1 = {
    "name": "Shubham",
    "age": 25,
    "city": "Mumbai"
}

# get(key[, default])	Get value by key
print(my_dict1.get('name'))
print(my_dict1.get('edu','NA'))

# items()- Returns a list of (key, value) tuples
print(my_dict1.items())

# keys()	Returns a list of all keys	d.keys()
# values()	Returns a list of all values	d.values()

# update(dict2) - 	Updates dict with another dict if key exists it updates the key's value  with current one if not then add that key value
my_dict1.update({'city':'Pune','edu':'PG'})
print(my_dict1)

# copy()-	Returns a shallow copy
dict_cp = my_dict1.copy()
print(dict_cp)

# setdefault(k, v)	Sets value if key is missing it add new key with dafault value
my_dict1.setdefault('ph No.','+91')

print(my_dict1)


# fromkeys(seq, val)	-Creates dict from sequence of keys
samp_dict = dict.fromkeys(["a", "b"],0) #→ {'a': 0, 'b': 0}
print(samp_dict)


# looping through dict
for key in my_dict1:
    print(key,my_dict1[key])


for key,val in my_dict1.items():
    print(f'{key} => {val}')


# 🔹 Dictionary Comprehension
sqrs = {
    x: x*x for x in range(1,5)
}

print(sqrs)


# 🔹 Example Use Case
inventory = {
    "apple": 10,
    "banana": 5
}

# Add more apples
inventory["apple"] += 5

print(inventory)

# Check stock
if "banana" in inventory:
    print(f"Bananas left: {inventory['banana']}")



# ///Sets
# sets is collection of non-repetative ele.
s = set()
s.add(1)
s.add(2)

print(s,type(s))

dic = {} #empty dict

# how to make empty sets
emp_set = set()
print(type(emp_set))

# dont user emp_set = {} as it will create empty dict

# set aumatically removes repeated elemnets while execution
s = {10,24,99,33,5,7,33,2,44}
print(s, type(s))


# set aumatically removes repeated elements while execution
s1 = {'Shubh',4,1,2002,23}
print(s1, type(s1))


# PROPERTIES OF SETS
#1.sets are unorderd - order of element doent matter here 
# 2. sets are unindexed - u cant access ele by indexes like list and string
# 3. there is no way to change items in set
# 4.sets cant contains duplicate values 

# sets operations 