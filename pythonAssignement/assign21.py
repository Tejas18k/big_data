# Find the product of each digit of number 
# i/p -->enter no :234
# o/p-->24

def prod(n):
    product = 1
    while n>0:
         rem=n%10
         product=rem*product
         n=n//10
    return product

i=int(input("enter no :"))
print(prod(i))


   
