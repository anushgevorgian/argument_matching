def print_product_details(name, price, quantity):
    print(f"Product Name: {name}")
    print(f"Price: {price}")
    print(f"Quantity: {quantity}")


product = {
    "name": "apple",
    "price": 100,
    "quantity": 5,
}

print_product_details(**product)
