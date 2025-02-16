#Collection in python 
#Exception Handeling

try:
    a=input("Enter a Number:")
    b=input("Enter a Number:")
    
    res=a/b
    
    print(res)
except TypeError:
    print("Pass values in integer")
except ZeroDivisionError:
    print("PCan not divide with zero")
except SyntaxError:
    print("syntax error might not passed all values")
except:
    print("Something is wrong!!!")
else:
    print("else execute whin program success")
finally:

'''
ETA--End Of Time Allocate
RCA-- Root Cause Analysis
Icidenet
Fix --Test--> Check-->prod-->check-->fixed bug
EOD--End Of Day
P-->priority 
p1--High priority
p2-- Medium priority
p3-- Less Priority'''
