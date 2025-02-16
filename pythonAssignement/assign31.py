#List all numbers divisible by 3 , 9 & 12 using nested "if" with List Comprehension


from re import I


mylist4 = [i for i in range(201) if i % 3 == 0  if i % 9 == 0 if i % 12 == 0]
print(mylist4)


l1 = [print("{} is Even Number".format(i)) if i%2==0 else print("{} is odd number".format(i))] # type: ignore
print(l1) # type: ignore

# Using list comprehension to generate a list of strings indicating even or odd
l1 = ["{} is Even Number".format(i) if i%2==0 else "{} is odd number".format(i) for i in range(10)]
# Printing each element of the list
for statement in l1:
    print(statement)
