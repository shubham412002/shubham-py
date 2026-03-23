

# 
# for i  in range(1,5):
#     print('# ',end='')

# print()

# for i  in range(1,5):
#     print('# ',end='')

# print()

# pattern1
# # # #
# # # #
# # # #
# # # #

# for i in range(1,5):
#     for i  in range(1,5):
#         print('# ',end='')

#     print()


# i = 1
# while i <= 4:
#     j = 1
#     while j <= 4:
#         print('# ', end='')
#         j += 1
#     print()
#     i += 1



# pattern2

#
# #
# # #
# # # #

# for i in range(1,5):
#     for j in range(i):
#         print('# ',end='')

#     print()
    

# or
# print('======')

# for i in range(4):
#     for j in range(i + 1):
#         print('# ',end='')

#     print()



# print('======')

# for i in range(1,5):
#     for j in range(5 - i):
#         print('# ',end='')
#     print()


# pattern1
# # # #
# # # #
# # # #
# # # #

# for i in range(4):
    # for j in range(4):
    #     print('# ', end="")
    # print()


# pattern2
# 
# # 
# # #
# # # #

# for i in range(4):
#     for j in range(i + 1):
#         print('# ', end="")
#     print()




# pattern3
# # # #
# # # 
# # 
# 

# for i in range(4):
#     for j in range(4 - i):
#         print('# ', end="")
#     print()


# pattern3
# 1 2 3 4
# 2 3 4
# 3 4
# 4

# for i in range(4):
#     for j in range(i,4):
#         print(j + 1,end=' ')
#     print()


# Printing the pattern
# Printing the pattern
# Printing the pattern
for i in range(4):  # Outer loop for rows
    for j in range(4):  # Inner loop for columns
        if j <= i:
            print(chr(65 + j), end=' ')  # Print letters A, B, C, etc.
        else:
            print(chr(79 + j - i), end=' ')  # Print letters O, P, Q, etc.
    print()  # Move to the next line
