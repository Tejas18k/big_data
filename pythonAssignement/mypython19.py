

def finalprice(price,discount=10):
    final_price=price-(price*(discount/100))
    print(final_price)
    
finalprice(100,25.0)
finalprice(100)