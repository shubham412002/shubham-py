# f = open('harry-python/file.txt')
# data = f.read()
# print(data)

import os

print(os.getcwd())
file_path = "harry-python/file.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as f:
        print(f"File found: {file_path}")
        # Read and print the file content
        file_content = f.read()
        print("File Content:")
        print(file_content)
else:
    print("File not found:", file_path)


# writing in file
str = "Shubh is learnign python"
f = open("harry-python/file2.txt", "w")
f.write(str)
f.close()


# more file funbction
# readlines() function
# f = open("harry-python/file1.txt", "r")
# lines = f.readlines()
# print(lines, type(lines))
# f.close()


# readline
# f = open("harry-python/file1.txt", "r")

# line1 = f.readline()
# print(line1, type(line1))


# line2 = f.readline()
# print(line2, type(line2))

# line3 = f.readline()
# print(line3, type(line3))

# print('using loop')
# f = open("harry-python/file1.txt", "r")

# line = f.readline()

# while(line != ""):
#     print(line)
#     line = f.readline()

# f.close()




# append mode
# str = ". Shubh is learnign python."
# f = open("harry-python/file.txt", "a")
# f.write(str)

# f.close()



# with in file

# f = open('file.txt')
# data = f.read()
# print(data)

# can be written as
with open('harry-python/file.txt') as f:
    print(f.read())

# dont need to close the file