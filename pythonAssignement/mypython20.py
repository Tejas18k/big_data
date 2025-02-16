

'''
variable argument
passing one or more that one paramamter values
it takes only for second paramamter not in first argrument
'''

def add(a,*b):
    temp=0
    for x in b:
        temp=temp+x
    res=a+temp
    print(res)
    
add(10)
add(10,20,20)
    