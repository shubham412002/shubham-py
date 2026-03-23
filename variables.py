num =  10
print(id(num))

name = 'Shubh'
print(id(name))


a = 10
b = a
print(id(a))
print(id(b))


# python is memory effcient if both variab;es contains same data they will point to same address
num1 = 101
num2 = 101
print(id(num1))
print(id(num2))

num3 = 101
print(id(num3))


a1 = 10

b1 = a1

print(id(a1))
print(id(b1))

b1 = 9

print(id(a1))
print(id(b1))

print(type(b1))

b5 = 3.98
print(type(b5))


str = 'Shubham'
print(type(str))

