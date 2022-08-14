

def only_floats(a,b):
    
    for i in str(a):
        if i == ".":
            
            a = float(a)

    for i in str(b):
        if i == ".":
            b = float(b)
    
    
    
    x = isinstance(a, float)
    y = isinstance(b, float)
    if x and y == True:
        return 2
    elif x == True and y == False:
        return 1
    elif x == False and y == True:
        return 1
    else:
        return 0


def main():
    a = input("Digit: ")
    
    b = input("Digit: ")
    
    print(only_floats(a, b))


if __name__ == "__main__":
    main()