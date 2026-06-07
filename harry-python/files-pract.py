import os

print(os.getcwd())

# reading fm file 
f = open("shubham-py/harry-python/file.txt", "r")
data = f.read()
print(data)


# writing to a file 
str1 = "learning python today123"

f = open('shubham-py/harry-python/sample.txt','w')
f.write(str1)
f.close()


# more file functions
# readline() -  rad each line one by one at a time 
f = open('shubham-py/harry-python/poem.txt', 'r')
line1 = f.readline()
line2 = f.readline()
line3 = f.readline()
print(line1)
print(line2)
print(line3)

# After the three readline() calls, the file pointer has already moved past the first three lines. so if u rinboth functions at same time but realines will read onl ramaining lines as pointerr aleady read those lines in readline

f.seek(0)
# to read all lines
lines = f.readlines()
print(lines)
f.close()


# to keep saprate and to skip f.close() each time use with


with open('shubham-py/harry-python/poem.txt', 'r') as f:
    l1 = f.readline()
    l2 = f.readline()
    l3 = f.readline()

    print(l1)
    print(l2)
    print(l3)

with open('shubham-py/harry-python/poem.txt', 'r') as f:
    lines = f.readlines()

    print(lines)



# read all lines from file using readline 
with open('shubham-py/harry-python/poem.txt', 'r') as f:
    line = f.readline()
    while(line != ''):
        print(line)
        line = f.readline()



# modes of opening a file
# r - reading file
# w - writing file 
# a - appeding file
# + - open for updating
# rb - read in binary 
# rt - read in binary


# | Mode           | Behavior                                               |
# | -------------- | ------------------------------------------------------ |
# | `'w'` (write)  | Erases existing content and writes from the beginning  |
# | `'a'` (append) | Keeps existing content and adds new content at the end |

with open('shubham-py/harry-python/file3.txt', 'w') as f:
    line = f.write('test user')
    print(line)

with open('shubham-py/harry-python/file3.txt','a') as f:
    line = f.write('\ntesting user')
    print(line)