# Python Program to Find the Largest Among Three Numbers

def find_largest(x,y,z):
    if x >= y and x >= z:
        return x
        print(x," is largest")
    elif y >= x and y >= z:
        return y
        print(y," is largest")
    else :
        return z 
        print(z," is largest") 

n1=int(input("enter 1st no :"))
n2=int(input("enter 2nd no :"))
n3=int(input("enter 3rd no :"))

print("Largest no is",find_largest(n1,n2,n3))  # Output
    
