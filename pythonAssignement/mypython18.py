'''
Scope of function

global

define outside of any function
or
uese word global

local
inside the function only
'''


'''

a=10 #global

def f1():
    print("This is Function 1")
    print(a)

def f2():
    print("This is Function 2")
    print(a)
    
f1()
f2()

'''


'''
#local
def f1():
    a=10
    print("This is Function 1")
    print(a)

def f2():
    print("This is Function 2")
    print(a)                #get error
    
f1()
f2()
'''


#local variable can make global 
def f1():
    global b
    b=23 #locals variable
     #mkaing local as global variable
    print("This is Function 1")
    print(b)

def f2():
    print("This is Function 2")
    print(b)              #get error
    
f1()
f2()



