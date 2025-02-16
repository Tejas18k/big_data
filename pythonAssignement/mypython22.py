#Annanamous Function or Lambda function
'''
x=lambda n:n*n*n
y=lambda a,b:(a+b)
z=lambda a,b:(a+b)*2


print(x(5))
print(y(2,5))
print(z(12,5))
'''
'''
------------------------


Higher order function

Function which takes or accept another function as parameter

map
filter
map accepet two parameter 1st is function and second is the sequenece or list
'''


'''
def sqr(n):
    return n*n
    
ls=[2,34,32,43,34,3,3]

res=map(sqr,ls)
print(res)

in map number of input equal to number of output
-----------

'''
'''
#find the table which is multiple of 10
def mulby_ten(v):
    return v*10
r=range(1,11)
res=map(mulby_ten,r)

# for x in res:print(x) in 3.x version we need to write for loop for print 
print(res)


-------------
'''

'''
#passing lambda function as parameter 

ls=[2,34,32,43,34,3,3]

res=map(lambda n:n*n,ls)
print(res)
------------------
'''
'''
e.g
r=range(1,12)
res=map(lambda n:n*10,r)

print(res)

'''
#Filter
#its a higher order function which apply on the condition and filter it according to it and fetch the result


#e.g 
#filter(iseven,range(1,11)
#it will perform element from 1 to 1o which is even


'''
r =range(1,11)
res_even=filter(lambda n:n%2==0,r)
print(res_even)

res_odd=filter(lambda n:n%2!=0,r)# or res_odd=filter(lambda n:n%2==1,r) 
print(res_odd)
'''

#reduce ------> 

reduce function takes n number of output and reduce it or aggarigate it into single result

e.g 1
ls=[11,22,33,44,55,66,77,88,99]
res=reduce(lambda x,y:x+y,ls)
print(res)

e.g 2

ls=[1,3,2,4,2]     #it take x=1 and y=3 then add x+y i.e 4
                   #then takes x=4 and y=2 then add i.d 6
                   #then takes x=6 and y=4 then add i.d 10
                   #then takes x=10 and y=2 then add i.d 12 which is final output
                   

res=reduce(lambda x,y:x+y,ls)
print(res)

------------------------

shift+alt+down arrow -->select multiple lines

ctrl+D ----crussor should at end use for repeat the line

ctrl + F --> replace
wrap around check whole file



to delete the specific word with its specific line

select that word press ctrl bookmark it and then remove

backtick --> `rank`
