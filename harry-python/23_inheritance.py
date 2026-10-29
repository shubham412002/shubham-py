class Employee:
    company = "ITC"
    name = "Shubh"
    salary = 1300000
    def show(self):
        print(f"name is {self.name} and salary is {self.salary}")



# class Programmer:
#     company = "ITC Infotech"
#     def show(self):
#         print(f"name is {self.name} and salary is {self.salary}")
    
#     def showLang(self):
#         print(f"the name is {self.name} he is good with {self.language}")

# here for same work using show() method in  both classes which is wrong so use DRY with inheritance


class Programmer(Employee):
    company = "ITC Infotech"
    
    def showLang(self):
        print(f"the name is {self.name} he is good with {self.language}")


a = Employee()
b = Programmer()

print(a.company,b.company)

a.show()
b.show() #show is now also available to programmers obj as well

# here Emlpoyee is Parent.base class and programmer is child /derived class 


# types of inheritance 
# 1.single 
# 2.multiple 
# 3. multilevel 

# single from parent to child refer above example 


# eg. multiple
class Employee:
    company = 'ITC'
    name = "Shubh"

    def __init__(self,salary):
        self.salary = salary

    def show(self):
        print(f"name is {self.name} and salary is {self.company} with salary {self.salary}")


class Coder:
    language = "Python"
    def printLanguages(self):
        print(f'I prefer to code in {self.language}')


class Programmer(Employee,Coder):
    company = 'ITC'

    # opt1
    # def __init__(self):
    #     super().__init__(120000)

    # opt2 pass salary as optional so that if we pass whi;e creating objectit will asogn that or else keep default one
    # def __init__(self,salary = 230000):
    #     super().__init__(salary)

    def showLanguages(self):
        print(f"name is {self.company} and good with {self.language}")


a = Employee(1200000)
b = Programmer(1300000) #if calss dont have own constructor it will call parent comtructor on  obj creation so it required to pass salary even its not there in class


# b = Programmer() #if we dont pass salary here we neeed to call init of parent means Employee class cause show is expecting salary there and as thi class dojnt have its own init construtor method its required with salary attribute 

b.show()
b.printLanguages()
b.showLanguages()

print(b.language)
# now b can access all methods 


#why its required to pass salary in b = Programmer(1300000)  also as its called only in Employee constructor?
# =>
# Good question. This happens because **`Programmer` inherits from `Employee`**.

# When you create:


# b = Programmer(1300000)


# Python looks for a constructor (`__init__`) in `Programmer`.


# class Programmer(Employee, Coder):
#     pass


# Since `Programmer` does **not** have its own `__init__`, Python automatically uses the first parent's constructor according to the MRO (Method Resolution Order).

# You can see it:


# print(Programmer.__mro__)


# Output:


# (<class '__main__.Programmer'>,
#  <class '__main__.Employee'>,
#  <class '__main__.Coder'>,
#  <class 'object'>)


# So:


# b = Programmer(1300000)


# is effectively treated as:


# Employee.__init__(b, 1300000)


# Therefore `salary` must be supplied.

# ---

# ### What if Programmer has its own constructor?


# class Programmer(Employee, Coder):

#     def __init__(self):
#         print("Programmer constructor")


# Now:


# b = Programmer()


# works because Python finds `Programmer.__init__()` first and stops searching.

# But:


# b.show()


# will fail because `Employee.__init__()` never ran, so `salary` was never created.

# To initialize the parent as well:


# class Programmer(Employee, Coder):

#     def __init__(self, salary):
#         super().__init__(salary)
#         print("Programmer constructor")


# Now:


# b = Programmer(1300000)


# calls:

# 1. `Programmer.__init__()`
# 2. `Employee.__init__()` via `super()`
# 3. `self.salary` gets created

# ---

# Think of inheritance like this:


# Programmer
#    ↓
# Employee
#    ↓
# object


# When an object is created, Python searches for `__init__` from top to bottom:


# Programmer.__init__ ?
#     ↓ No
# Employee.__init__ ?
#     ↓ Yes
# Use it


# That's why `Programmer(1300000)` requires the same arguments as `Employee.__init__()` when `Programmer` doesn't define its own constructor.



# 3. multilevel 
class Employee:
    a = 1


class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee
print(o.a)

p = Programmer()
print(p.a)
print(p.b)

m = Manager()
print(m.a)
print(m.b)
print(m.c)




# Super method--
# super() method used to access methods of a super class in the derived class 
# for eg. super().__init__() - calls constructor of base class inside derived class

class Employee:
    a = 1

    def __init__(self):
        print('constructor of Employee called')

class Programmer(Employee):
    b = 2

    def __init__(self):
        print('constructor of Programmer called')

    def showRole(self):
        print(f'programmer with id {self.b}')

class Manager(Programmer):
    c = 3
    mngId = 34

    def __init__(self):  
        # super().__init__() #ran constructor of parent
        super().showRole() #accessed method from parent class 
        print('constructor of Manager called')

    @classmethod
    def manageWork(cls):
        print(f'my mnager id is {cls.mngId}')


# o = Employee()
# print(o.a)

# p = Programmer()
# print(p.a)
# print(p.b)

m = Manager()
print(m.a)
print(m.b)
print(m.c)

m.mngId = 4
print(m.mngId) #this will print 4 cause we have assigned 4 to object 
m.manageWork() #this will still refer to class attribute as mentioned as class attribute 






# Class method-- @classmethod
# class method is method which bound to class not with object of the class

class Employee:
    a = 2

    @classmethod #without this it will refer to object with self parameter but with class method u will walys refer to class attribute
    def show(cls):
        print(f'the class value of a is {cls.a}')
    

e = Employee()
e.a = 4 
e.show()



# property decorators 

class Employee:
    a = 2

    @classmethod #without this it will refer to object with self parameter but with class method u will walys refer to class attribute
    def show(cls):
        print(f'the class value of a is {cls.a}')

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(' ')[0]
        self.mname = value.split(' ')[1]
        self.lname = value.split(' ')[2]
    

emp = Employee()
emp.a = 4 
emp.show()

emp.name = "Shubh Sunil Patankar"
print(emp.name)
print(emp.fname)
print(emp.lname)

# using @property() made one property to be set  by user but using that we are creating two new propeties on same class which is running behind asking name but setting fname and lname 

# see in above example from user are asking his full name but to name only assigning fname and lname



# In Python, property decorators allow you to control access to class attributes while keeping the syntax simple (obj.attribute instead of obj.get_attribute()).

# The three main decorators are:

# @property → Getter
# @<property_name>.setter → Setter
# @<property_name>.deleter → Deleter (less commonly used)


# using getter with @property--
class Employee:
    def __init__(self,salary):
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    

emp = Employee(60000)
print(emp.salary) #looks like attribute access but the method is being called BTS


# Using Setter--
class Employee:
    def __init__(self,salary):
        self._salary = salary
    
    @property
    def salary(self):
        return self._salary
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            raise ValueError('Salary cant be 0')
        
        self._salary = value
    

emp = Employee(60000)
print(emp.salary)
emp.salary = 70000 #calls setter means @proprty 

print(emp.salary) #calls getter 



# calculate email of employee by name for company account 
class Employee:
    def __init__(self,name):
        self.name = name
    
    @property
    def email(self):
        return f"{self.name.lower()}@company.com"
    

emp1= Employee('Shubh')
print(emp1.email)




# operator overloading --

class Number:
    def __init__(self,n):
        self.n = n

    def __add__(self, num):
        print(self,num)  # it calls __str__ or else it  will print objects
        print(self.n,num.n)
        return self.n + num.n
    
    def __str__(self):
        return str(self.n)
    
n = Number(2)
m = Number(3)

print(n + m)

# other overloadingmethods are 
# __sub__ - substraction
# __mul__ - multilpicatiion
# __truediv__- / devision
# __floordiv__ - // floor division
# __str__ - used to set what gets displayed upon calling print 
# __len__ - overides len()

