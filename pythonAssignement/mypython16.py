

'''

def sqr(n):
    res=n*n
    return res


add=sqr(1)+sqr(7)+sqr(9)+sqr(11)+sqr(14)+sqr(16)+sqr(18)

print(add)


----------------------------------------
'''


#pass 1 number find sqr and cube than addtion of both numbers 

num=input("Enter a number:")

num=int(num)

def sqr(n):
    return n*n

def cube(n):
    return n*n*n
   
x=sqr(num)
y=cube(num)

print(x+y)
