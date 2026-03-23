
# Sets
# collection of unique el

s = {3,6,4}
print(s)
print(type(s))

# for making empty set dont use {} as it creates empty dict
es = set()
es.add(2)
es.add(4)

print(es)



# set can contain value of any data type
s2 = {3,6,4,67,7.8,'Sanket'}



# sets methods
# add()
s2.add('Gaurav')
print(s2)

# clear- removes all ele from set 
# s2.clear()

# copy() returns shallow copy of set
new_s2 = s2.copy()
print(new_s2)

# diffrence()- returns new set with ele that are not present in another set 
s3 = {1,2,3}
s4 = {3,4,5}

print(s3.difference(s4))

# sets are unordered
# unindexed
# sets are immutable means u cant change exting value but you can add or remove that
# they cant contains duplicate value

# remove()
# set = {4,6,8,9,9,456}
# set.remove(8)
# set.remove(1) causes error 
# print(set)


# pop()
# removes random ele 
# s.remove()


# union-collect all values on both sets without repetation
set5 = {1,2,3,4,5}
set6 = {4,5,6,7,8}

print(set5.union(set6))


# intersection-all common value in new set
set5 = {1,2,3,4,5}
set6 = {4,5,6,7,8}

print(set5.intersection(set6))


#
# dic = {
#     'Guru': 'Teacher',
#     'Dua' : 'Blessings',
#     'Ishwar':'God'
# }

# word = input('Enter word thar u want to search for:')

# print(dic[word])



# 
# num_set = set()

# for i in range(0,8):
#     num = int(input(f'Enter num {i + 1} to add'))
#     num_set.add(num)

# print(num_set)


#
# samp_set = set()
# samp_set.add(18)
# samp_set.add('18')
# print(samp_set)


# what will be length of set
# samp_set = set()
# samp_set.add(18)
# samp_set.add(18.0)
# samp_set.add('18')

# print(samp_set)


# s = {} 
# print(type(s))


d = {} 

for i in range(0,3):
    name = input('enter friend\'s name:')
    lang = input('enter lang name:')
    d.update({name:lang})

print(d)    


