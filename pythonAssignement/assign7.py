# even and odd

'''
def even_odd(x=11):
    if x%2==0 :
        return "eneterd number is even"
    else:
        return "entered number is odd"
    
print(even_odd())

'''

#or
def even_odd(x):
    if x%2==0 :
        return "eneterd number is even"
    else:
        return "entered number is odd"
    

num=int(input("enter the number:"))

print(even_odd(num))


