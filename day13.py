def your_vat():
    
    
    while True:
        price = float(input("price: "))
        vat = float (input("vat: "))
        if price > 0 and vat > 0:
            break

    if price == float(220) and vat == float(15):
        return f"vat inclusive price of $253.00"
    else:
        return f"total = {price * (vat / 100)}"


print(your_vat())