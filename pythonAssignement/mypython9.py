'''for i in ["sun","mon","tus","wed","fri","sat"]:
    for y in ["working","holiday"]:
        print(i,y)
        
        cmd
        PS C:\Users\HP> python D:/mypython9.py
('sun', 'working')
('sun', 'holiday')
('mon', 'working')
('mon', 'holiday')
('tus', 'working')
('tus', 'holiday')
('wed', 'working')
('wed', 'holiday')
('fri', 'working')
('fri', 'holiday')
('sat', 'working')
('sat', 'holiday')
'''

for x  in ["sun","mon","tus","wed","fri","sat"]:
    for y in ["weekdays","weekend"]:
        if (x in ("sat","sun")) and (y in ("weekend")):
            print(x,y)
        if (x not in ("sat","sun")) and (y not in ("weekend")):
            print(x,y)