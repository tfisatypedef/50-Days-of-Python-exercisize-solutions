register = {'Michael':'yes','John': 'no',
'Peter':'yes', 'Mary': 'yes'}


def register_check(poop):
    up = 0
    for key in poop:
        #print(poop[key])
        if poop[key] == "yes":
            up = up + 1
    return up 

def main():
    print(register_check(register))


if __name__ == "__main__":
    main()