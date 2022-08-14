
def my_discount():
    price = float(input("price: ").strip("$"))
    disc = float(input("discount: ").strip("%"))
    
    poop = price - (price * (float(disc)/ 100))

    print(f"${poop}")


my_discount()