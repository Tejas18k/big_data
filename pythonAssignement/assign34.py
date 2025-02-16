#res1 = (lambda **kwargs: sum(kwargs.values())) # This lambda function can take an
#print(res1(a = 10 , b= 20 , c = 30))

#-----------


#def sqr(n):
#    return n*n
#    
#ls=[2,34,32,43,34,3,3]
#
#res=map(sqr,ls)
#print(res)





#----------------map function ---------


#find the table which is multiple of 10
#def mulby_ten(v):
#    return v*10
#    
#r=range(1,11)
#
#res=map(mulby_ten,r)
#print(res)
#
##or
#result_list = list(res)
#print(result_list)
#-----------------------
#-----------------------map function with lambda---------------------------
#numbers = [1, 2, 3, 4, 5]
#result = map(lambda x: x * 2, numbers)
#print(list(result))
##-----------------------filter function with lambda---------------------------
#result = filter(lambda x: x %2==0, numbers)
#print(list(result))

#-----------------------reduce function---------------------------

numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result) 