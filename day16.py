def sum_list():
    poop =  [[2, 4, 5, 6], [2, 3, 5, 6]]
    pee = [one for sublist in poop for one in sublist]
    print(sum(pee))
def main():
    sum_list()


main()