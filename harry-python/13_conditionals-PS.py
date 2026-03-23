# Q1 find greatest of 4 numbers
# nums = []
# for i in range(0,4):
#     num = int(input('enter number:'))

#     nums.append(num)


# nums.sort()

# print(nums)
# print('max is:',nums[len(nums) - 1])


# OR
# max_num = 0

# for i in  range(0,4):
#     num = int(input('enter number:'))

#     if num > max_num:
#         max_num = num


# print("The greatest number is:", max_num)



# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# total_marks_per_subject = int(input('enter total max marks for each sub:'))

# std_marks = []

# passed_each_subject = True

# for i in range(1,4):
#     marks = int(input(f'enter marks of subject {i} out of 100:'))

#     std_marks.append(marks)

#     if marks < 0.33 * total_marks_per_subject:
#         passed_each_subject = False

# total_obt_marks = sum(std_marks)

# print(len(std_marks) )
# print(std_marks)

# percentage_marks =(( total_obt_marks) / (len(std_marks) * total_marks_per_subject)) * 100

# print(std_marks)
# print(total_obt_marks)
# print(percentage_marks,'%')

# if passed_each_subject and percentage_marks >= 40:
#     print("The student has passed.")
# else:
#     print("The student has failed.")

# 0R

# Input maximum marks for each subject
total_marks_per_subject = int(input('Enter total max marks for each subject: '))

# List to store marks of 3 subjects
std_marks = []

for i in range(1, 4):
    m = int(input(f'Enter marks of subject {i} out of {total_marks_per_subject}: '))
    std_marks.append(m)

# Calculate total obtained marks
total_obt_marks = sum(std_marks)

# Calculate total maximum marks for all subjects
total_max_marks = len(std_marks) * total_marks_per_subject

# Calculate percentage
percentage = (total_obt_marks / total_max_marks) * 100

# Print results
print("Marks in each subject:", std_marks)
print("Total obtained marks:", total_obt_marks)
print("Percentage:", percentage, "%")

subject_pass = all(m >= (0.33 * total_marks_per_subject) for m in std_marks)

# Final Pass/Fail decision
if percentage >= 40 and subject_pass:
    print("Result: Pass 🎉")
else:
    print("Result: Fail ❌")

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# p1 = "Make a lot of money"
# p2 ="buy now"
# p3 ="subscribe this"
# p4 =" click this"

# msg = input('enter comment')

# if((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
#     print('spam comment')
# else:
#     print('not a spam comment')




# 4. Write a program to find whether a given username contains less than 10
# characters or not.

# usr_name = input('enter user name:')

# if len(usr_name) <= 10:
#     print('pls enter at least 10 letters')
# else:
#     print('correct user name')


# 5. Write a program which finds out whether a given name is present in a list or not.
# lst = ['Shubham',"Sham","Sunil","Sayli"]

# name = input('enter to search in  list:')

# print([n.lower() for n in lst])

# if name.lower() in [n.lower() for n in lst]:
#     print('name is present in list')
# else:
#     print('its not present')



# 6. Write a program to calculate the grade of a student from his marks from the
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F


# mark = int(input('enter marks:'))

# if(mark <= 100 and mark >= 90):
#     grade = 'EX'
# elif(mark <= 90 and mark >= 80):
#     grade = 'A'
# elif(mark <= 80 and mark >= 70):
#     grade = ''
# elif(mark <= 70 and mark >= 60):
#     grade = 'C'
# elif(mark <= 60 and mark >= 50):
#     grade = 'D'
# elif(mark <= 50 ):
#     grade = 'F'

# print('Grade is',grade)



# Write a program to find out whether a given post is talking about “Harry” or not

post = input('Write a post')

if("Harry".lower() in post.lower()):
    print('post is about harry')
else:
    print('not relevant')



