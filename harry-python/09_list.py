# list are containers to store list of values of any data type
lst = ['Apple',"Orange", 5,7.78,False]

print(lst[0])
print(lst[0][0])

# lst[0][0] = 'B' causes an error cause strings are immutable


# lists are mutable
# changing items in list 
lst[0] = "Grapes"
print(lst)


# slicing in list
print(lst[1:4])

# list methods
# as strings are immuatble they always return new string but lists methods change org. string
lst.append('Aakash')
print(lst)


nums = [3,7,8,4,10,6]
nums.sort()
print(nums)


nums.reverse()
print(nums)


# to add ele at specific index
lst.insert(2,"Tomatoes")
print(lst)

# to remove ele at specific index
res = lst.pop(3)
print(res)#returns removed ele
print(lst)


# remove ele byits value
lst.remove(7.78)
print(lst)


