try:
    a=input("Enter a Number:")
    b=input("Enter a Number:")
    
    res=a/b
    
    print(res)
except TypeError:
    print("Pass values in integer")
except ZeroDivisionError:
    print("PCan not divide with zero")
except SyntaxError:
    print("syntax error might not passed all values")
except:
    print("Something is wrong!!!")
else:
    print("else execute whin program success")
finally:
    print("always run even program success or fail")
    
    
    meta data will be update 
    so in hdfs update is not support therefor hive not support storage data into hdfs 
    it store it in derby or in metastore
    
    
    new partion 
    you have 10 cites then how to delete onw city
    1st hdfs folder deleter
    2nd delete folder
    3rd delete metadata
    then msck repair table tablename(it refersh the data)