

def convert_add(n):
    sump = []
    for i in n:
        
        sump.append(int(i))
    
    return sum(sump)

def main():
    piss = []
    try:
        while True:
            piss.append(input("C: "))
    except EOFError:
        print("\nSum: ", end="")

    print(convert_add(piss))


if __name__ == "__main__":
    main()