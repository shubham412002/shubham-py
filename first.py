print("Shubh")
x = 3
y = 4
res = x + y
print(res)


name = 'Youtube'
print(name)
print(name[4])
# print(name[8])

print(name[-1])


# slicing in  string
print(name[0:3])

print(name[2:5])

# without end para it wil stop at end
print(name[3:])

# without start para it wil start from first char
print(name[:4])

# if end para is not exists then it will end at last char in string
print(name[2:16])


# changing string char at specific indexes will not work strings in py are immutable
# name[0:3] = "My"
# print(name)

# other way is to use slicing
print('My' +  name[3:]) 


myname = "Shubham Sunil Patankar"
print(len(myname))


# res = eval(input('enter a expression'))
# print(res)


x = 8 
r = x % 2

if r == 0:
    print('Even')
    if x > 4:
        print('great')
    else:
        print('small')
else:
    print('odd')


# elif
z = 3 
if z == 1:
    print(1)
elif z == 2: 
    print(2)
elif z == 3: 
    print(3)    
else:
    print('not matched')