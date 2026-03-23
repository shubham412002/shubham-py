# 1. Write a program to print multiplication table of a given number using for loop.
# n = int(input('Enter a number:'))

# for i in range(1,11):
#     print(f"{n} X {i} = {i * n}")


# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]
# greet = 'Hi, Welcome'

# for p in l:
    # print(p)
    # .lower()
    # if(p.startswith('s')):
    #     print(f"{greet} {p}")





# 3. Attempt problem 1 using while loop.
# n = int(input('Enter a number:'))
# i = 1

# while i <= 10:
#     print(f"{n} X {i} = {i * n}")
#     i += 1




# 4. Write a program to find whether a given number is prime or not.
# num = int(input('Enter a number:'))

# if num == 0 or num == 1:
#     print(num, "is not a prime number")
# elif num > 1:
#     for i in range(2, num):
#         if (num % i) == 0:
#             print(f'{num} Not a prime number')
#             print(i,"times",num//i,"is",num)
#             break
#     else:
#         print(f'{num} is prime number')
 

# 5. Write a program to find the sum of first n natural numbers using while loop.
# num = int(input('Enter a number:'))

# sum  = 0
# i = 0

# while i <= num:
#     sum += i
#     i += 1

# print(f"The sum of the first {num} natural numbers is {sum}.")


# 6. Write a program to calculate the factorial of a given number using for loop.
# num = int(input('Enter a number:'))

# fact = 1

# if num < 0:
#     print('fact not exists')
# elif num == 0:
#     print('fact of 0 is 1')
# else:
#     for i in range(1, num +1):
#         fact = fact * i
#     print("The factorial of",num,"is",fact)




# 7. Write a program to print the following star pattern.

'''
  *
 ***
***** 
'''

# for n = 3

# n = 3
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i -1),end="")
#     print('') 


# for n = 5
'''
    *
   ***
  ***** 
 ********
**********
'''

# n = 5
# for i in range(1,n+1):
#     print(" " * (n-i),end="")
#     print("*" * (2*i - 1),end="")
#     print('')


# end="" is used to print the output in the same line cause print statement by default prints in new line

# 7. Write a program to print the following star pattern.

'''
*
**
***
****
***** 
'''

# for n = 5


# n = 5  
# for i in range(0,n+1):
#     print("*" * (i),end="")
#     print('')



# Write a program to print the following star pattern.

'''
*
***
*****
*******
'''


# n= int(input('enter number:'))

# for i in range(1,n+1) :
#     print('*' * (2 * i - 1), end="")
#     print('')


# 9. Write a program to print the following star pattern.
'''
* * *
*   * 
* * * 
'''

# for n = 3

n = int(input('Enter a number:'))
for i in range(1,n+1):
    if i == 1 or i == n:
        print('*'* n,end="")
    else:
        print('*',end="")
        print(" " * (n-2),end="")
        print('*',end="")
    print('')


# 10. Write a program to print multiplication table of n using for loops in reversed order
# n = int(input('Enter a number:'))

# for i in range(10,0,-1):
#     print(f"{n} X {i} = {i * n}")
