def total_price(apples_price, bananas_price, bread_price,/, tax=0.1):
    total = (apples_price+bananas_price+bread_price)*(1+tax)
    return total

print(total_price( 100, 200, 500, tax=0.2))