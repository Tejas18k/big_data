#Python Program to Multiply two Floating Point Numbers

def mul_float(x,y):
    return x*y
    print(x*y)

num1=float(input("enter the 1st no : "))
num2=float(input("enter the 2nd no : "))
print("the product of two no is ", mul_float(num1,num2))

#o/p --> ('the product of two no is ', 6.820000000000001)

#print (mul_float(num1,num2))

#--------------------------------------------------------------------------


def mul_float(x, y):
    return x * y

num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))
result = mul_float(num1, num2)
print("The product of the two numbers is: %f" % result)

# just test
