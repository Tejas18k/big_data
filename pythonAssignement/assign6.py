#Python Program to Swap Two Numbers
'''
a=int(input("enter no :"))
b=int(input("enter the no:"))


a = a + b
b = a - b
a = a - b

print("value of a is ", a)
print("value of b is ", b)

'''

#--------------------------------


def swap(a,b):
    a = a + b
    b = a - b
    a = a - b
    return a,b 


num1=int(input("enter no:"))
num2=int(input("enter no:"))

x=swap(num1,num2)
print(x)

             #want  o/p enter new value of a=4 and b=3 

#---------------------------- 

# Original values
a = 5
b = 10

# Swapping values using tuple unpacking
a, b = b, a

print("After swapping, a =", a)
print("After swapping, b =", b)

#ask sir 