def calculate_discount(price, discount_percent):
    
    if discount_percent>=0.2:
        total = price  - (price*discount_percent)
        return total
    else:
        return price
 
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount_price: "))
total=calculate_discount(price, discount_percent)
print(total)
