# Finding maximum number in the list
'''
li=[22,44,21,78,98,34,73]

max=li[0]
for x in li:
    if x>max:
        max=x
print(max )
'''
#--------------------



# Finding maximum number in the list using built-in function max()

'''
li=[22,44,21,78,98,34,73]
print(max(li))

#---------------------
'''



#Finding maximum number in the list using user define function max()


def max_num(list):
    max=list[0]
    for x in list:
        if x>max:
            max=x
    return max

num=(input("enter list:"))
print(max_num(num))
