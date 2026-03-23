a = 5
b = 31.9
fname = "Shubh"
print(type(fname))  # <class 'str'>
print(type(a))  # <class 'int'>
print(type(b))  # <class 'float'>

# type casting
# converting one data type to another
b1 = '31.3'
# we cant convert float string directly to int
fltb = int(float(b1))

print(fltb)

strNum = '35'
print(int(strNum))

fltb = float(b1)
print(fltb)

intb = int(fltb)
print(intb)

g = 56
print(type(str(g)))


# examples of type 
print(int('32'))#str to int
print(float('32.6'))#str to float 
print(str(31))#int to str

# input func -
num1 = int(input('enter a num1-'))
num2 = int(input('enter a num2-'))

print(num1 + num2)  