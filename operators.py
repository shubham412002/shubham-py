# arithmatic-- +,-,%,/,*

# assignment-- =,!=
x = 5
x = x + 2
print(x)

x += 2
print(x) 

x *= 3
print(x)

# assigning multiple values at same time
a,b = 5,6
print(a)
print(b)


# relational 
res = a > b
print(res)

res = a < b
print(res)

res = a >= b
print(res)

res = a <= b
print(res)


# logical --and, or and not
res = a > b and a < b
print(res)

res = a > b or a < b
print(res)

res = not a > b
print(res)

res = a != b
print(res)


# unary
n = 7

n = -n
print(n)


# type and type casting 
a = "31.3"

b = float(a)

print(b)
print(type(b))