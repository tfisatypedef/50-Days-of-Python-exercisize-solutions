

def zeroed(n):
    n[-1] = 0
    n[0] = 0
    return n

def main():
    try:
        poopy = []
        while True:
            poop = int(input("nums pls: "))
            poopy.append(poop)
    except EOFError:
        print("\n")
        pass
    
    print(zeroed(poopy))


if __name__ == "__main__":
    main()
