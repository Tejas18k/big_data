from sys import argv

username=argv[1]
password=argv[2]

if username =="Admin" and password=="tejas@123":
 print("login successful")
else:
 print ("login failed")
 
 '''
 cmd
 
C:\Users\HP>python D:\mypython4.py "Admin" "Tejas@123"
login successful'''


 
 