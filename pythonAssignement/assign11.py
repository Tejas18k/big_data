# Python Program to Check Leap Year

def check_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):       
       return True
    else:
       return False

y = int(input("Enter a year: "))

if(check_leap_year(y)):
    #print(y,"is a leap year.")
    print("{} is leap year !!!".format(y))
else:
    #print(y,"is not a leap year.")
    print("{} is not leap year!!!".format(y))

#or
#----------------------------------------------------
'''
def check_leap_year(year):
    if (year % 4 == 0 and year % 100 !=0) or (year % 400 == 0):       
        print(year,"is leap year")
    else:
        print(year,"is not leap year")
    
y = int(input("Enter a year: "))
print(check_leap_year(y))  # Output: 2020 is leap year
'''


