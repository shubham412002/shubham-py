# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not 
# present, a message without exiting the program must be printed prompting the same. 
try:
    with open("1.txt",'r') as f:
        data = f.read()
        print(data)
except Exception as e:
    print(e)

try:
    with open("2.txt",'r') as f:
        f.read()
except Exception as e:
    print(e)

try:
    with open("3.txt",'r') as f:
        f.read()
except Exception as e:
    print(e)

    
# with advance python common open
try:
    with (
        open("1.txt", "r") as f1,
        open("2.txt", "r") as f2,
        open("3.txt", "r") as f3,
    ):
        print(f1.read())
        print(f2.read())
        print(f3.read())

except FileNotFoundError as e:
    print(f"File not found: {e.filename}")

except PermissionError as e:
    print(f"Permission denied: {e.filename}")

except OSError as e:
    print(f"OS Error: {e}")

except Exception as e:
    print(f"Unexpected error: {e}")
    
    
    
# If an interviewer specifically asks you to **use multiple file opening at once** and **handle exceptions**, they're usually testing whether you understand how context managers work—not whether you can make missing files magically continue.

# The correct answer is to explain the limitation.

# ### Solution 1: Standard way (Most interviewers expect this)

# ```python
# try:
#     with (
#         open("1.txt", "r") as f1,
#         open("2.txt", "r") as f2,
#         open("3.txt", "r") as f3,
#     ):
#         print(f1.read())
#         print(f2.read())
#         print(f3.read())

# except FileNotFoundError as e:
#     print(f"File not found: {e.filename}")

# except PermissionError as e:
#     print(f"Permission denied: {e.filename}")

# except OSError as e:
#     print(f"OS Error: {e}")

# except Exception as e:
#     print(f"Unexpected error: {e}")
# ```

# ### What you should say in the interview

# > "Using a single `with` statement with multiple context managers is an all-or-nothing operation. If opening any file fails, Python automatically closes any files that were already opened, skips the `with` block, and transfers control to the `except` block. This guarantees proper resource cleanup."

# This explanation is often more important than the code.

# ---

# # Interview Follow-up

# Suppose:

# ```
# 1.txt  ✔
# 2.txt  ❌ Missing
# 3.txt  ✔
# ```

# Execution:

# ```
# Open 1.txt  ✔
# Open 2.txt  ❌ Exception
# Close 1.txt automatically ✔
# Never attempts 3.txt
# Jump to except
# ```

# This demonstrates that you understand how multiple context managers behave.

# ---

# # If the interviewer says:

# > "I want to read whichever files exist."

# Then tell them:

# > "A single `with` statement cannot do that because if any context manager fails to enter, the entire statement aborts. In that case, I'd open each file independently, typically in a loop."

# Example:

# ```python
# files = ["1.txt", "2.txt", "3.txt"]

# for file in files:
#     try:
#         with open(file, "r") as f:
#             print(f"{file}:")
#             print(f.read())
#     except FileNotFoundError:
#         print(f"{file} not found")
# ```

# ---

# # Senior-level interview answer ⭐

# A strong answer is:

# > **Interviewer:** "Open three files at once and handle exceptions."
# >
# > **You:** "Certainly. If the requirement is to use a single `with` statement, I'll wrap it in `try-except`. However, I'd like to point out that multiple context managers are atomic: if any `open()` fails, the remaining files won't be opened, and any previously opened files will be closed automatically. If the business requirement is to process available files independently, I would instead use separate `with` statements or iterate through the file list."

# That answer demonstrates:

# * ✅ Knowledge of context managers
# * ✅ Understanding of exception handling
# * ✅ Awareness of resource cleanup
# * ✅ Ability to choose the right approach for the requirement

# That's the kind of reasoning interviewers typically look for, especially for Python developers with some experience.


# 2. Write a program to print third, fifth and seventh element from a list using enumerate 
# function. 
l = [1, 2, 3, 4, 6, 7, 8, 9]

for i, el in enumerate(l):
    if i >= 2 and i < 7:
        if i % 2 == 0:
            print(el)


l = [1, 2, 3, 4, 6, 7, 8, 9]

for i, el in enumerate(l):
    if i == 2 or i == 4 or i == 6:
        print(el)
        

l = [1, 2, 3, 4, 6, 7, 8, 9]

for i, el in enumerate(l, start=1):
    if i in (3, 5, 7):
        print(el)
        

# 3. Write a list comprehension to print a list which contains the multiplication table of a 
# user entered number. 
num = int(input("enter a number to generate table:"))

mulTbl = [num * i for i in range(1,11)]
print(mulTbl)

# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by 
# handling the ‘ZeroDivisionError’. 
try:
    a = int(input('Enter a num1:'))
    b = int(input('Enter a num2:'))
    
    d = a / b
    print(d)

except ZeroDivisionError as e:
    print('Infinite')
    


# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt. 
num = int(input("enter a number to generate table:"))

mulTbl = [num * i for i in range(1,11)]
print(mulTbl)

with open('shubham-py/harry-python/chp12-PS.py/Tables.txt','a') as f:
    f.write(f"Table of {num}: {str(mulTbl)} \n")
    