# 1. Write a program using functions to find greatest of three numbers.

# def largeOf3(n1,n2,n3):
#     large = 0
#     if(n1 > n2 and n1 > n3):
#         large = n1
#     elif(n2 > n1 and n2 > n3):
#         large = n2
#     else:
#         large = n3
    
#     return large

# l = largeOf3(3,4,5)
# print(l)


# 2. Write a python program using function to convert Celsius to Fahrenheit.

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# # Example usage
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C = {fahrenheit:.2f}°F")



# 3. How do you prevent a python print() function to print a new line at the end.
# print('name')
# print("Hello ", end="")  # Prevents a newline
# print("World!") 

# 4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum(num):
#     if num <= 0:
#         return 0
#     return num + sum(num-1)

# num = int(input("Enter a positive integer: "))

# res = sum(num)
# print(res)


# def sum(num):
#     if num <= 0:
#         return 0
#     return num + sum(num-1)

# num = int(input("Enter a positive integer: "))

# res = sum(num)
# print(res)




#  Write a python function to print first n lines of the following pattern:

'''
***
** 
*
'''

# - for n = 3
# n = 3

# def pattern(n):
#     if(n==0):
#         return
#     print("*" * (n))
#     pattern(n - 1)

# pattern(n)

# def pattern(n):
#     if n == 0:
#         return
#     pattern(n - 1)
#     print("*" * n)

# n = int(input("Enter a number: "))
# pattern(n)

# OR
# n = int(input("Enter a number: "))
# for i in range(1, n + 1):
#     print("*" * i)

# 6. Write a python function which converts inches to cms.
# n = 7

# def inc_to_cm(i):
#     return i * 2.54

# print(inc_to_cm(n))


# 7. Write a python function to remove a given word from a list ad strip it at the same
# time.

# def rem(l,word):
#     n = []
#     for item in  l:
#         # if (item != word):
#             n.append(item.strip(word))
#     return n


# l = ["Shubham","Harray","Rohan","an"]

# print(rem(l,'an'))

# def rem(l, word):
#     n = []
#     for item in l:
#         stripped_item = item.strip()  # Remove spaces from the item
#         if stripped_item != word:  # Check if it's the target word
#             n.append(stripped_item)
#     return n

# # Example list
# l = ["Shubham", "Harray", "Rohan", " an "]

# # Remove the word "an"
# print(rem(l, 'an'))


# 8. Write a python function to print multiplication table of a given number.
# def table(n):
#     for i in range(1,11):
#         print(f"{n} X {i}  = {n * i}")
        

# num = int(input('Enter a number:'))

# table(num)