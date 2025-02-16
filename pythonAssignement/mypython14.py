# Taking user inputs
pname = input("Enter product which you purchase: ")
price = float(input("Enter each unit price: "))
qty = int(input("Enter total qty which you bought: "))
discount = float(input("Enter discount in number: "))

# Defining the function
def final_price(pname, price, qty, discount):
    # Calculate total price and discount
    total_price = price * qty
    total_dis = total_price * (discount / 100)
    final_price = total_price - total_dis
    
    # Display the result
    print("For {0} {1}, you have saved {2:.2f} and you need to pay only {3:.2f} rs.".format(qty, pname, total_dis, final_price))

# Calling the function
final_price(pname, price, qty, discount)
