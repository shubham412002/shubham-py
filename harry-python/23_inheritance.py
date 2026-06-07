class Employee:
    company = "ITC"
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
