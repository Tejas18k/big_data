




name=input("enter the name of product:")
price=input("enter the price:")
qty=input("enter the total qty:")
dis=input("enter the discount you get:")


price=float(price)
qty=int(qty)
dis=float(dis)

Total_price=price*qty
discount=Total_price*float(dis)/100
final_price=Total_price-discount

print(final_price)




