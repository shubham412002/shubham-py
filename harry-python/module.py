def myFunc():
    print('Hello world')
    
    
print(__name__)
    
if __name__ == "__main__":
    # this code direct;y executed by running file the file its present in
    print('We are directly running thid code')
    myFunc()
    print(__name__)

# __name__ it will print __main__ if u run this same file but if u import this in another file and run the same it will print the module name means its file name