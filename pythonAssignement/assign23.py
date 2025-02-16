'''
def sum_of_sqr(n):
    sum=0
    temp=n
    while n>0:
        rem=n%10
        product=rem*rem
        sum=sum+product
        n=n//10

        if sum==temp:
            return True
        else:
            return False

    

i=int(input("enter no :"))

if(sum_of_sqr(i)==True):
    print("sum of square of digit is equal to original number")
    print("Amstrong number")
else:
    print("sum of square of digit is not equal to original number")
    print("Not Amstrong number")
'''
#--------------------

def sum_of_sqr(n):
    sum = 0
    original_n = n  # Store the original value of n
    while n > 0:
        rem = n % 10
        sum += rem * rem
        n //= 10
    return sum == original_n

i = int(input("Enter a number: "))

if sum_of_sqr(i):
    print("Sum of squares of digits is equal to the original number")
    print("Armstrong number")
else:
    print("Sum of squares of digits is not equal to the original number")
    print("Not an Armstrong number")
