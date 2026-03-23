# find numbers divisible by 5 
# nums = [12,59,78,78,22,56,213,112]

# for num in  nums:
#     if num % 5 == 0 :
#         print(num)
#         break
# else:
#     print('not found')


# program to check prime number
num = int(input('Enter a number:'))

for i in range(2,num):
    if num % i == 0:
        print('Not Prime')
        break
else:
    print('Prime')