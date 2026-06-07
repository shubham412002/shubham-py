# class is blueprint for creating objects.
# object is the instantiation of the class. Class is defined its template is defined
# memory is allocated to object only after its instatition


# Object of the given class can invoke the methods available to it without revealing implementation details to user is called abstraction and encapsulation

# naming conentions for class and object
# Noun  -> Class -> Employee 
# Adjectives ->  Attribute -> name,age,salary
# Verbs -> Methods -> getInfo(),getIncr()

# eg. 
class Employee:
    language = "Py" #class attributes 
    salary  = 1200000

# here  all of above are class attributes they directly belongs to class

shubh = Employee()
shubh.name = "Shubham" #obect /instance attributes 
print(shubh.name,shubh.language, shubh.salary)

roh = Employee()
roh.name = 'Rohan'
print(roh.name,roh.language, roh.salary)

#  here name is instance / object attribute and salary, languages are class attributes as they directly belongs to the class 
# instnace attribute always takes prefernece over class attribute during assignment and retrieval

# for eg
class Employee:
    language = "Py" #class attribute
    salary  = 1200000

shubh = Employee()
shubh.language = "js" #instance attributes 
print(shubh.language)


# self parameter - 
# self parameter refers to instance of the class.Its automatically passed with a function call from an object

# shubh.getSalary() #here self is harry 
# same as Employee.getSalary(shubh)

class Employee:
    language = "Py"
    salary  = 1200000

    def getInfo(self):
        print(f'{self.name} is having salary {self.salary}')
    
    def greet(self):
        print('hello Shubh')

shubh = Employee()
shubh.name = "Shubham"
shubh.language = "js" 

# shubh.getInfo()  Employee.greet() takes 0 positional arguments but 1 was given this error will come if dont pass self parameter
# its same as Employee.getInfo(shubh) so to point object while execution we have to use self parameter
shubh.greet()


# Static Methods 
# If we dont want anyh method to use self parameter then we have to assign that method as static method.
# just like greet in below example dont require any object related things so mark itr as static method
# in this case will not get any error even without any self

class Employee:
    language = "Py"
    salary  = 1200000

    def getInfo(self):
        print(f'{self.name} is having salary {self.salary}')

    @staticmethod
    def greet():
        print('hello Shubh')

shubh = Employee()
shubh.name = "Shubham"
shubh.language = "js" 

shubh.getInfo() 
shubh.greet()


# Contructors / init method in python--
# __init__ - init is speacial method which runs first as soon as object is created
# __init is known as constructor method
# its takes self and any required further arguments

# parameters passed with init are necessary to pass while creati8ng object or else u will get error
#  Employee.__init__() missing 1 required positional argument: 'name

# for eg
# class Employee:
#     company = 'Google'
#     salary = 1200000
    
#     def __init__(self,name):
#         self.name = name
    
#     def getSalary(self):
#         print(f"{self.company} employee has salary {self.salary}")


# emp1 = Employee('Shubh')
# emp1.getSalary()


class Employee:
    language = "Py"
    salary  = 1200000

    def __init__(self,name, salary,lang):
        print('constructor called')
        self.name = name
        self.salary = salary
        self.language = lang 

    def getInfo(self):
        print(f'{self.name} is having salary {self.salary} with {self.language} language')

    @staticmethod
    def greet():
        print('hello Shubh')


shubh1 = Employee('Shubham',1300000,'JS')
# shubh1.name = "Shubham"
print(shubh1.name,shubh.salary,shubh1.salary)

shubh1.getInfo()

tej = Employee('Tejas',50000,'Java')
tej.getInfo()

#IN python methods ahoch start and ends with __ are called dunder methods


