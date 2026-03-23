num = 2.5
print(type(num))

num = 3
print(type(num))

num = 3 + 4j
print(type(num))

# conversions
a = 3.4
b = int(a)
print(type(b))

c = float(b)
print(c)
print(type(c))


k = 2
l = 7
d = complex(k,l)
print(d)


# bool 
tf = k > l
print(tf)

tf = k < l
print(tf)

print(int(True))
print(int(False))

print(type(tf))


lst = [23,45,56,78,90]
print(type(lst))

s = {23,45,67,45,67,89,34,56,23}

print(s)
print(type(s))


t = (23,45,67,88,78,97)
print(t)
print(type(t))

str = "Shubh"
print(str)
print(type(str))


# typerange and its conversion to list
range(10)
print(type(range(10)))
print(range(10))
print(list(range(10)))


# creating list of even numbers till 10 with range 
print(list(range(2,10,2)))



# dict
d = {
    'Shubh':"Vivo",
    "Rani":"Poco",
    'Pappa':'Oppo',
    'Mummy':'Mi'
}

print(type(d))
print(d.keys())
print(d.values())
print(d['Shubh'])

print(d.get('Pappa'))