#Python Program to Calculate the Sum of Natural Numbers

# for loop
'''
def sum_of_natural_numbers(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a positive integer: "))
print("The sum of natural numbers up to {} is {}".format(n, sum_of_natural_numbers(n)))
'''
#-----------------------------------
# while loop
def sum_of_natural_no(num):
    sum=0
    i=1
    while i<=num:
        sum=sum+i
        i=i+1
    return sum 

n = int(input("Enter a positive integer: "))
print("The sum of natural numbers up to {} is {}".format(n, sum_of_natural_no(n)))


