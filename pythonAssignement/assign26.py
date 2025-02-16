#Finding minimum number in the list using user define function 

def find_min(list):
    
    min=list[0]
    for x in list:
        if x<min:
            min=x
    return min

num=(input("enter list:"))
print(find_min(num))

#-----------------------


li=[22,44,21,78,98,34,73]
print(min(li))