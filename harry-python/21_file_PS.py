# practice set
# Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# poem = open('harry-python/poem.txt')
# content = poem.read()

# print(content)

# if 'twinkle' in content.lower():
#     print('Twinkle is present')
# else:
#     print('Twinkle is not present')

# poem.close()



# 2. The game() function in a program lets a user play a game and returns the score
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
# contains the previous Hi-score. You need to write a program to update the Hiscore whenever the game() function breaks the Hi-score.


# import random

# def game():
#     print('This is a game')
#     score = random.randint(1, 100)
#     # read the exting hiscore
#     with open('harry-python/hi-score.txt') as f:
#         hiscore = f.read()

#         if hiscore != '':
#             hiscore = int(hiscore)
#         else:
#             hiscore = 0

#     print('Current score is:', score)

#      if score is greater than high score write it to that file
#     if score > hiscore:
#         with open('harry-python/hi-score.txt', 'w') as f:
#             f.write(str(score))
#         print('Congrats! You have broken the hiscore')


#     return score

# game()


# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
# different files. Place these files in a folder for a 13 – year old.

# def generate_table(num):
#     with open(f'harry-python/tables/mul_table_of_{num}.txt', 'w') as f:
#         for i in range(1, 11):
#             f.write(f'{num} X {i} = {num*i}\n') 

# for i in range(2, 21):
#     generate_table(i)
#     print(f'Multiplication table of {i} is generated')



# create tables using tables string and write that into the file
# def  generate_table(num):
#     table = ""
#     for i in range(1,11):
#         table += f"{num} X {i} = {num*i}\n"

#     print(table)
#     with open(f'shubham-py/harry-python/new-tables/table{num}.txt','w') as f:
#         f.write(table)
 
# for i in range(2,21):
#     generate_table(i)
#     print(f'multiplication table of {i} created')


# if dont have tables folder then create it
# import os

# Function to generate a multiplication table
# def generate_table(num):
    # Ensure the folder exists
    # folder_path = 'harry-python/tables'
    # os.makedirs(folder_path, exist_ok=True)  # Create folder if it doesn't exist
    
    # Create and write the multiplication table file
    # with open(f'{folder_path}/mul_table_of_{num}.txt', 'w') as f:
    #     for i in range(1, 11):
    #         f.write(f'{num} X {i} = {num * i}\n')

# Generate multiplication tables from 2 to 20
# for i in range(2, 21):
#     generate_table(i)
#     print(f'Multiplication table of {i} is generated')





# 4. A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file

# with open('harry-python/temp.txt') as f:
#     content = f.read()

#     print(content)

#     if 'Donkey' in content:
#         print('Donkey is present')
#         content = content.replace('Donkey', '#####')

#         with open('harry-python/temp.txt', 'w') as f:
#             f.write(content)
# f.close()



# 5. Repeat program 4 for a list of such words to be censored.
# words = ['Donkey', 'bad', 'Ganda', 'hindi', 'Animal']

# Open the file and read the content
# with open('harry-python/temp1.txt', 'r') as f:
#     content = f.read()

# print("Original Content:\n", content)

# Replace each word (considering all case variations)
# for word in words:
    # Replace all case variations of the word
    # content = content.replace(word, '#' * len(word))  # Original case
    # content = content.replace(word.capitalize(), '#' * len(word))  # Capitalized case
    # content = content.replace(word.upper(), '#' * len(word))  # Uppercase
    # content = content.replace(word.lower(), '#' * len(word))  # Lowercase
    # content = content.replace(word.title(), '#' * len(word))  # Title case

# Write the updated content back to the file
# with open('harry-python/temp1.txt', 'w') as f:
#     f.write(content)

# print("\nUpdated Content:\n", content)






# 6. Write a program to mine a log file and find out whether it contains ‘python’.
# with open('harry-python/log.txt') as f:
#     content = f.read()

# if 'python' in content.lower():
#     print('Python is present')
# else:
#     print('Python is not present')



# 7. Write a program to find out the line number where python is present from ques 6.
# line_no = 1
# found = False
# with open('harry-python/log.txt') as f:
#     lines = f.readlines()

# for line in lines:
#     if 'python' in line.lower():
#         found = True
#         print(f'Python is present in line number {line_no}')
#         break
#     line_no += 1
# else:
#     if not found:
#         print('Python is not present in the file')

# f.close()

# Solutiuon 2
# with open('harry-python/log.txt') as f:
#     lines = f.read()

# word = 'python'
# lineno = 1
# for line in lines:
#     if word in line:
#         print(f'{word} is present in line {lineno}')
#         break
#     lineno +=  1

# else:
#     print(f'{word} is present in line {lineno}')


# Solution 3
# with open('harry-python/log.txt') as f:
#     for line_no, line in enumerate(f, start=1):
#         if 'python' in line.lower():
#             print(f'Python is present in line number {line_no}')
#             break
#     else:
#         print('Python is not present in the file')

# 8. Write a program to make a copy of a text file “this. txt”
# with open('harry-python/this.txt') as f:
#     content = f.read()

# with open('harry-python/this_copy.txt', 'w') as f:
#     f.write(content)

# f.close()



# 9. Write a program to find out whether a file is identical & matches the content of another file.
# with open('harry-python/poem.txt') as f:
#     content1 = f.read()

# with open('harry-python/this_copy.txt') as f:
#     content2 = f.read()

# if content1 == content2:
#     print('Files are identical')
# else:
#     print('Files are not identical')


# 10. Write a program to wipe out the content of a file using python.
# with open('harry-python/this_copy.txt', 'w') as f:
#     f.write('')

# 11. Write a python program to rename a file to “renamed_by_ python.txt.
# import os
# os.rename('harry-python/this_copy.txt', 'harry-python/renamed_by_python.txt')

