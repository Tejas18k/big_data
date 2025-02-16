'''from sys import argv

username=argv[1]
password=argv[2]

if username =="Admin":
     if password=="Tejas@123":
          print("login done successfully !!!")
     else:
         print("please enter the valid password !!!")
else:
 print( "please enter the valid username ")
 
 cmd
 
C:\Users\HP>python D:\mypython6.py "Admin" "Tejas@123"
login done successfully !!!

C:\Users\HP>python D:\mypython6.py "Admin" "Tejas@12"
please enter the valid password !!! '''


#---------------------------------------- or -----------------------------------
'''
from sys import argv
username=argv[1]
password=argv[2]

if username =="Admin":
 if password=="Tejas@123":
         print("login done successfully !!!")
 else:
         print("please enter the valid password !!!")
else:
  print( "please enter the valid username ")

cmd 
C:\Users\HP>python D:\mypython6.py "Admin" "Tejas@12"
please enter the valid password !!!

'''

#--------------------------------------------------------------or--------------------------------------



username = input("Enter your username: ")
password = input("Enter your password: ")

if username == "Admin":
    if password == "Tejas@123":
        print("login done successfully !!!")
    else:
        print("please enter the valid password !!!")
else:
    print("please enter the valid username")

cmd

C:\Users\HP>python D:\mypython6.py
Enter your username: "Admin"
Enter your password: "Tejas@123"
login done successfully !!!