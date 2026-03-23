d = {} #empty dictionary
# dictionary is collection of key-value pairs
d = {
    "Name" : "Shubh",
    "Age":22,
    "DOB": "04-Jan-2002",
    "Job":"Soft DEV"
}

# on place of u can also have int,float,list,tuple,dict
# key should be unique


print(d["DOB"])
print(d["Age"])
print(d)
# its is unordered 

# mutable
d["Age"] = 23
print(d)

# indexed but can index with key name 
d["Age"]
# d[0] its incorrect 
# it cant contains duplicate value
# if u have assigned sa me key ro vale it takes last assigned value to that key

# methods
# items- returns list of (key,val) with tuples
print(d.items())

# • a.keys(): Returns a list containing dictionary's keys.
print(d.keys())

# update • a.update({"friends":}): Updates the dictionary with supplied key-value pairs.if key is not there it adds that key value pair
d.update({"Name":'Shubh Patankar',"Nationality":'Ind'})
print(d)


# a.get("name"): Returns the value of the specified keys 
print(d.get('Job'))


d.get("Age") #it rertun none if key doesnt match
d["Age"]#it rertun error if key doesnt match 



# dict methods
# dict.keys()
# Returns a view object with all keys in the dictionary.
my_dict = {"a": 1, "b": 2}

print(my_dict.keys())




# dict.values()
# Returns a view object with all values in the dictionary.

print(my_dict.values())  # Output: dict_values([1, 2])


# dict.items()
# Returns a view object with key-value pairs as tuples.
print(my_dict.items())  # Output: dict_items([('a', 1), ('b', 2)])


# dict.update([other_dict])
# if key will not be there it will add that key value pair
# Updates the dictionary with key-value pairs from another dictionary or iterable.
my_dict.update({"c": 3,'d':4})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'c': 3}


# dict.pop(key[, default])
# Removes the specified key and returns its value. If the key is not found, returns default (if provided).

value = my_dict.pop("b")
print(value)  # Output: 2
print(my_dict)


# dict.popitem()
# Removes and returns the last key-value pair as a tuple
last_item = my_dict.popitem()
print(last_item)  # Output: ('c', 3)


# dict.clear()
# Removes all items from the dictionary.
# my_dict.clear()
# print(my_dict)  # Output: {}


# dict.get(key[, default])
# Returns the value for a key, or default if the key is not found.

my_dict = {"a": 1}
print(my_dict.get("a"))  # Output: 1
print(my_dict.get("b", "Not found"))  # Output: Not found



# key in dict
# Checks if a key exists in the dictionary.

print("a" in my_dict)  # Output: True


new_dict = my_dict.copy()
print(new_dict)


# dict.setdefault(key[, default])
# Returns the value of the key if it exists. Otherwise, sets the key to default and returns default.
value = my_dict.setdefault("b", 10)
print(value)  # Output: 10
print(my_dict)  # Output: {'a': 1, 'b': 10}4


# dict.fromkeys(iterable[, value])
# Creates a new dictionary with keys from the iterable and sets all values to value (default is None).
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}






