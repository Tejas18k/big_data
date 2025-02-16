# Python Program to Display Fibonacci Series
'''
def fibonacci(n):
    a = 0
    b = 1
    
    # Check is n is less
    # than 0
    if n < 0: 
        print("Incorrect input")
        
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
      
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for i in range(1, n):
            c = a + b
            a = b
            b = c
        return b

print(fibonacci(9))
'''
#-------------------

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter the number of terms: "))
print("Fibonacci Series:")
for i in range(n):
    print(fibonacci(i)),
