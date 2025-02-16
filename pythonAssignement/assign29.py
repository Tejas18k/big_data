# remove duplicate from list
'''
def remove_duplicate(list1):
    uqe_list=[]
    for i in list1:
        if i not in uqe_list:
            uqe_list.append(i)
    return uqe_list

ilist=input("enter list :")
result=remove_duplicate(ilist)
print(result)

'''

def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates, then back to a list
    return list(set(input_list))

# Example usage
input_list = [1, 2, 2, 3, 4, 4, 5, 5, 5]
result = remove_duplicates(input_list)
print("List with duplicates removed:", result)
 