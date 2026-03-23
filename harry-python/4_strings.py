#Strings 
# Strings are immutable in python
a = 'Shubh'
b = "Shubh"
c = '''Shubh
Patankar'''#multiline string

# strings slicing 
nm = "shubham"
print(len(nm))
print(nm[2:5])#from index 2 - 5 without including 5 means till 4
print(nm[:5]) #0-4  
print(nm[-5:])#to length
# negative slicing
print('slicing--',nm[-5:-2])
print('slicing2--',nm[-2:-4])#empty string as invalid index tracing

# slicing with skip value
str1 = "amazing"
print(str1[1:6:2])



# string functions
str2 = 'Shubham Patankar'
# 1.len
print(len(str2))

# 2.startswith - returns true/false , case sensitive
print(str2.startswith('shu'))

# 3.endswith - returns true/false , case sensitive
print(str2.endswith('kar'))

#4. capitalize - capitalize first word only 
print(str2.capitalize())

# 5.lower -
print(str2.lower())

# 6.upper -
print(str2.upper())

# 7.title-Capitalizes the first letter of each word.
print(str2.title())

#8. count - counts numbers of chars in string
print(str2.count('a'))
print(str2.count('bh'))


# 9.find - returns index of first occurrence of word
print(str2.find('bh'))

# 10. replace - replace old word with new one in entire string
str1 = 'Hello world, Welcome to the new world'
print(str1.replace('world', 'word'))#replaces all occurrences


#extraa methods
# # str.swapcase()	Swaps case of each letter	"Hello".swapcase() → 'hELLO'

# str.rfind(s)	Finds last occurrence	"hello".rfind("l") → 3

# str.index(s)	Same as find but raises error if not found	"hello".index("e") → 1

# str.isdigit()	Checks if string is numeric	"123".isdigit() → True

# str.isalpha()	Checks if string has only alphabets	"abc".isalpha() → True

# str.isalnum()	Checks if alphanumeric	"abc123".isalnum() → True

# str.isspace()	Checks if string contains only whitespace	" ".isspace() → True
# str7 = 'shu pat '
# print(str7.isspace()) #=> false

# | `str.strip()`           | Removes leading/trailing spaces | `"  hello  ".strip()` → `'hello'`       |

# | `str.lstrip()`          | Removes leading spaces          | `"  hello".lstrip()` → `'hello'`        |

# | `str.rstrip()`          | Removes trailing spaces         | `"hello  ".rstrip()` → `'hello'`        |

# | `str.replace(old, new)` | Replaces substring              | `"hello".replace("l", "x")` → `'hexxo'` |




# str.split()- split strings based on separator provided
s = "Hello         World\tPython \nShubham"
result = s.split()
print(result)  # ['Hello', 'World', 'Python', 'Shubham']

s = "a,b,c"
result = s.split(",")
print(result)  # ['a', 'b', 'c']

s = "a,b,c,d"
result = s.split(",",2)
print(result)  # ['a', 'b', 'c,d']

# str.join(iterable)
# The string you're calling .join() on is the separator.
# Only works on iterables containing strings.

words = ['Hello', 'World']
res = ' '.join(words)
print(res)


# Example 2: Joining with hyphen
items = ['2025', '07', '27']
dtStr = "-".join(items)
print(dtStr)

# ⚠️ Error Example: Joining non-strings
nums = [1, 2, 3]
# " ".join(nums)  # ❌ TypeError

nums = [1, 2, 3]
str3='';
result = " ".join(map(str, nums))
print(result)  # '1 2 3'



# | Function            | Description         | Example                       |
# | ------------------- | ------------------- | ----------------------------- |
# | `str.center(width)` | Centers string      | `"hi".center(6)` → `'  hi  '` |
# | `str.ljust(width)`  | Left-aligns string  | `"hi".ljust(6)` → `'hi    '`  |
# | `str.rjust(width)`  | Right-aligns string | `"hi".rjust(6)` → `'    hi'`  |
# | `str.zfill(width)`  | Pads with zeros     | `"42".zfill(5)` → `'00042'`   |


# //escape sequence charachetrs
str4 = 'Shubh is good boy\nbut not a bad boy.'
print(str4)

str4 = 'Shubh is good boy\tbut not a bad boy.'
print(str4)

str4 = "Shubh is good boy but not a \"bad\" boy."
print(str4)

str4 = 'Shubh is good boy but not a \'bad\' boy.'
print(str4)

str4 = 'Shubh is good boy but not a \\bad\\ boy.'
print(str4)


# \b	Backspace	
print("Helloo\b556")	#Hello


# \a	Bell (sound alert)	
print("wwe\ahhh")	#(may beep)

# \v	Vertical tab (rare)	
print("A\vB")	#A[vertical tab]B
# \ooo	Octal value
print("\101")	#A
# \xhh	Hex value	
print("\x41")	#A


import os
os.system('echo -n "\a"')  # On Unix-like systems

# or
print('\a')  # Simple but often silent


import winsound
winsound.Beep(1000, 500)  # Beep at 1000 Hz for 500 ms
