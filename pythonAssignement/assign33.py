from sys import argv


marks=int(argv[1]) #marks=int(marks) both are same 

 

if marks>=75:
 print ("garde:distinction")
elif marks>=60:
 print ("garde:good")
elif marks>=45:
 print ("garde:Avarge")
elif marks>=35:
 print ("garde:poor")
else :
 print ("no need to study you are legand")
 