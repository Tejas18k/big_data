# Python Program to Compute Quotient and Remainder
'''
divident=int(input("enter the divident:"))
divisor=int(input("enter the divisor:"))

quotient= divident//divisor
reminder=divident % divisor

print(quotient)
print(reminder)
'''

#-------------------------

# with function

'''
def find_q_and_r(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

print(find_q_and_r(dividend,divisor))

o/p

Enter the dividend: 3
Enter the divisor: 1
(3, 0)
'''
#----------------------------------------------------------

def find_q_and_r(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder

dividend = int(input("Enter the dividend: "))
divisor = int(input("Enter the divisor: "))

quotient, remainder = find_q_and_r(dividend, divisor)
print("Given quotient is: {} and remainder is: {}".format(quotient, remainder))

