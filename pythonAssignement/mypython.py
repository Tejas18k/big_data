
r=10
area_of_circle=3.141*r*r
print(area_of_circle)





name="mobile"
price=25000
qty=2
dis=10

Total_price=price*qty
discount=Total_price*float(dis)/100
final_price=Total_price-discount

print(final_price)

#for 2 mobiles you have saved 5000 and you need to  pay only 45000 here

print("for {1} {0} you have saved {2} and you need 
to pay only {3}".format(name,qty,discount,final_price))
