#Python Program to Find Factorial of a Number

# using while loop
'''
n=int(input("enter num:"))
fact=1
while n>0:
    fact=fact*n
    n=n-1
print(fact)
'''
#or
'''
n=int(input("enter num:"))
fact=1
i=1
while i<=n:
    fact=fact*i
    i=i+1
print(fact)
'''


#using for loop


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    return fact

n=int(input("enter num:"))
call=factorial(n)




