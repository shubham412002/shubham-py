# types string notation
a = 'Shubh'
b= "Shhubh"
c = '''Shubh'''


# *** strings are immutable in python

# string slicing
str = "shubh"

print(str[:3])
print(str[2:])

print(len(str))



# slicing with skpip values
wrd ="Shubham Patankar"
print(wrd[1:5:2])

str = "ASDJHGFDSDFHGFDHGFDGC"
print(str[1:10])
print(str[1:10:2])


# string function
# len()-returns length of str

# both are case sensitive
# endswith
print(str.endswith('DGC'))

# startswith
print(wrd.startswith('shu'))

# capitalize
print(wrd.capitalize())

# lower()
# upper()

# title() -makes string like tittle case
print(wrd.title())


# find() find first occurrence of goven str
print(wrd.find('ubh'))
print(wrd.find('pat'))#this is case sensitive


# replace-used to replace old word by new one
print(wrd.replace('Pat','pat'))

# its replaces all occurences from string
s = 'Shubh is good good dev.'
print(s.replace('good','smart'))


# escape sequence charachters

v = "Shubh is good"


#  Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

resStr = letter.replace('<|Name|>','Shubham').replace('<|Date|>','12-12-2020')
print(resStr)

# Write a program to detect double space in a string.

str ="Shubh is  good Dev  "
print(str.find('  '))

# 4. Replace the double space from problem 3 with single spaces.
str ="Shubh is  good  Dev"
print(str.replace('  ',' '))


# 5. Write a program to format the following letter using escape sequence
# characters.
# letter = "Dear Harry, this python course is nice. Thanks!"

letter = "Dear Harry, this python course is nice. Thanks!"
print(letter)

formatted_letter = "Dear Harry,\n\tthis python course is nice.\nThanks!"
print(formatted_letter)





# string revision 
# string is sequence of charachter enclosed in double quotes
str1 = 'Shubh'
str2 = "Shubh"
str3 = '''Shubh''' # this is multiline string


# string is immutable - we cannot change the value of string

# string slicing [start:stop:step]
str4 = "Shubham Patankar"
print(str4[0:5])  # Slicing from index 0 to 4 5 is exclusive
print(str4[0:5:2])  # Slicing from index 0 to 4 with step 2

print(str4[-6:-3]) # Slicing from index -6 to -4 (exclusive)\

print(str4[4:])  # Slicing from index -6 to the end
print(str4[:6])  # Slicing from the start to index 5 (exclusive)


print(str4[0]) # Accessing the first character only one charachter at a time

lenStr = len(str4)  # Length of the string
print(lenStr)  # Output: 16


str5 = "Shubh"
print(str5[-7:-2])  # Slicing from index -7 to -3 (exclusive)
print(str5[1:4])  # Slicing from index 1 to 3 (exclusive)



# step / skip value`
str6 = "Shubham Patankar"
print(str6[1:5:2])  # Slicing from index 1 to 4 with step 2


# string functions
# len() - returns the length of the string
print(len(str6))  # Output: 15

# endswith() - checks if the string ends with the specified suffix
# this is case sensitive 
print(str6.endswith('kar'))  # Output: True

# startswith() - checks if the string starts with the specified prefix
# this is case sensitive
# str6 = "shubham patankar" for this string it will return False
print(str6.startswith('Shub'))  # Output: True

# Capitalize() - capitalizes the first character of the string
str6 = "shubham patankar"
print(str6.capitalize())  # Output: Shubham patankar

# count() - counts the occurrences of a substring in the string
# case sensitive
print(str6.count('a'))  # Output: 4 (counts 'a' in the string) 
print(str6.count('am'))  # Output: 1 (counts 'a' in the string)

# find() - finds the first occurrence of a substring in the string
print(str6.find('ham'))  # Output: 2 (index of first occurrence of 'ham')

# lower() - converts the string to lowercase
# upper() - converts the string to uppercase


