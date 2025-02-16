#2.accept name and salary of person and print in hand salary after 10% Tax and 7% Policy premium and 200 rs as PT.

#how to run----> cmd : python D:/p3.py "Karan" 100000

from sys import argv


print(argv[0]) # this statement is use to print filename

name=argv[1]
salary=int(argv[2])

def inhand_sal(name,salary):
    sal_after_tax=salary*0.83-200
    print("Hi {0} , your inhand salary is {1}".format(name,sal_after_tax))

inhand_sal(name,salary)
