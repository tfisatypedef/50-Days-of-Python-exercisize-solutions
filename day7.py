

def period(n):
    lst = [] 
    for i in range(n):
        lst.append(i)
        #print(i, sep=".", end="")

    print(*lst, sep=".")


def main():
    n = int(input("int pls: "))
    period(n)


main()