# varible name and rules to define variables
fname = 'Shubh'

_usrName = 'SPatankar'

# rules
# 1. Variable names can only contain letters, numbers, and underscores.
#    They cannot contain spaces or special characters (e.g., @, #, $, etc.).
#  varibales names should only start with a letter or an underscore.
# 2. Variable names cannot start with a number.
# 3. Variable names are case-sensitive.
# 4. Variable names cannot be a Python keyword (e.g., `if`, `else`, `while`, etc.).

# data types

# 1. Numeric - 
# 1a. int - whole numbers
age = 25
# 1b. float - decimal numbers
height = 5.9
# 1c. complex - complex numbers
complex_num = 3 + 4j

# 2.Sequence Types -
# 2a. str - string
name = "Harry"
# 2b. list - ordered collection of items
fruits = ["apple", "banana", "cherry"]
# 2c. tuple - immutable ordered collection of items
coordinates = (10.0, 20.0)

# 3. Dictionary / Mapping Type -
# 3a. dict - key-value pairs
person = {
    "name": "Harry",
    "age": 25,
    "city": "New York"
}

# 4. Set Types -
# 4a. set - unordered collection of unique items
unique_numbers = {1, 2, 3, 4, 5}

# 5. Boolean Type -
# 5a. bool - True or False values   
is_student = True

# 6. None Type -
# 6a. NoneType - represents the absence of a value
nothing = None


# 7. Binary Types -
# 7a. bytes - immutable sequence of bytes
binary_data = b"Hello, World!"

# 7b. bytearray - mutable sequence of bytes
mutable_binary_data = bytearray(b"Hello, World!")

# 7c. memoryview - allows access to the internal data of an object that supports the buffer protocol
memory_view = memoryview(binary_data)


