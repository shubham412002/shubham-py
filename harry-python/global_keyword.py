# global keyword is used to modify the variable outside the current scope

a = 89

def fun():
    global a #here we are referring to global variable 
    a = 4
    print(a)
    
fun()
print(a)