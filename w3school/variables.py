# varaible name must start with a letter or an underscore not with number
# variable can only contain letters, numbers, and underscores
# variable name cannot contain spaces



# Assigning a value to a variable
x = 5

# Display the value of x
print(x)

# assigning multiple value to multiple variable
x, y, z = 5, 10, 15
print(x)
print(y)
print(z)

# Assign the same value to multiple variables in one line
x = y = z = 10


# Global variable
# variable that are created outside of a function are known as global variable and can be used by any function
# Global variables can be used by everyone, both inside of functions and outside.

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# if we create same variable inside a function then it will be considered as local variable and that variable can only be used inside that function

# for ex
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)




