# its elegent way to create list based on exiting list 

# for eg find asqaures of each element of list 

l = [1,2,3,4,5,6]

# way 1
sqrdList = []
for i in l:
    sqrdList.append(i * i)

print(sqrdList)

# way 2
sqrs = [ i*i for i in l]

print(sqrs)

# eg 2
lst = [4,5,8,9,10,26,47]

lst1 = [i for i in lst if i > 8]

print(lst1)