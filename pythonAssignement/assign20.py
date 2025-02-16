
# Find the addtion of each digit of number 
#i/p-->123
#o/p-->6

def sumofnum(n):
     sum=0
     while n!=0:
        rem=n%10
        sum=sum+rem
        n=n/10
     
     return sum
        
        

        

num=int(input("enter the num:"))

print(sumofnum(num))


       
        