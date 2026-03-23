def avg(a,b,c):
    t = (a + b + c) / 3
    return t

avg1 = avg(3,4,5)
print(avg1)


avg2 = avg(23,56,76)
print(avg2)


# ending is dafult argument here
def greet(name,ending = 'Thanks'):
    print(f'Good Day, {name}. {ending}')


greet('Shubh')

greet('Shubh','Have a good day.')

# functions are of two types 
# built in - range(),print(),len()
# user defined-all above examples



# recursion

def fact(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * fact(n-1)

n = int(input('enter a number:'))
fact = fact(n)
print(fact)