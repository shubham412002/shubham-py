lst = ['Shubham','Rani',False,32]

i = 0
while(i < len(lst)):
    print(lst[i])
    i += 1

for i in range(5):
    print(i)


# range(start,stop,step_size) 
# for i in range(0,100,4):
#     print(i)


# for loop can be used on list,tuple,string
str = "Shubham"

for i in str:
    print(i)

l = [2,4,6,7,8]
for i  in l:
    print(i)


t = (3,6,8,89,90)
for i  in t:
    print(i)



# for loop with else
for i in range(5):
    print(i)
else:
    print('executes after completion')



# for loop with range function start,stop,step_size  
for i in range(0,10,4):
    print(i)
else:
    print('executes after completion')


t = (3,6,8,89,90)
for i  in t:
    print(i)