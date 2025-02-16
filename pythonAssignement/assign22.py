# Find the sum of square  of each digit of number
# i/p --> 123
#o/p --> 1*1 + 2*2 + 3*2 --> 14

def sum_of_sqr(n):
    sum=0
    while n>0:
        rem=n%10
        product=rem*rem
        sum=sum+product
        n=n//10
    return sum

i=int(input("enter no :"))
print(sum_of_sqr(i))