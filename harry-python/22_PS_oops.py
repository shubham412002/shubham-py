# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.
class Programmer:
    company = "Microsoft"

    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer('Shubh',1300000,421202)
print(p.name,p.salary,p.company,p.pin)

r = Programmer('Rahan',900000,421201)

print(r.name,r.salary,r.company,r.pin)



# 2. Write a class “Calculator” capable of finding square, cube and square root of a
# number.

class Calculator:

    def __init__(self,num):
        self.n = num

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n * self.n * self.n
    
    def squareroot(self):
        return self.n ** (1/2)
    
c = Calculator(4)
sq = c.square()
cb = c.cube()
sqrt = c.squareroot()

print(sq)
print(cb)
print(sqrt)


# 3. Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?

class Demo:
    a = 2

ob1 = Demo()
print(ob1.a)
ob1.a = 3

print(ob1.a)
print(Demo.a)

# class attrcbute will not change after changing obj. attribute



# 4. Add a static method in problem 2, to greet the user with hello.


class Calculator:

    def __init__(self,num):
        self.n = num

    def square(self):
        return self.n * self.n
    
    def cube(self):
        return self.n * self.n * self.n
    
    def squareroot(self):
        return self.n ** (1/2)
    
    @staticmethod
    def greet():
        print('hello user')
    
c = Calculator(4)
sq = c.square()
cb = c.cube()
sqrt = c.squareroot()

c.greet()

print(sq)
print(cb)
print(sqrt)




# 5. Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
import random as r

class Train:
    def __init__(self,trainNo):
        self.trainNo = trainNo
        
    def bookTicket(self,frm,to):
        print(f"Ticket is booked in trainNo {self.trainNo} from {frm} to {to}")

    def getStatus(self):
        print(f"Train {self.trainNo} is running on time")

    def getFare(self,frm,to):
        print(f"Ticket fare of Train {self.trainNo} from {frm} to {to} is {r.randint(500,5000)}")

tr = Train(100119)

tr.bookTicket('CSMT','Goa')
tr.getStatus()
tr.getFare('CSMT','Goa')






# 6. Can you change the self-parameter inside a class to something else (say
# “harry”). Try changing self to “slf” or “harry” and see the effects

class Demo:
    a = 2

    def __init__(slf,n):
        slf.n = n

ob1 = Demo(5)
print(ob1.a)
print(ob1.n)