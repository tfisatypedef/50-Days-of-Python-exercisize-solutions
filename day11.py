def equal_strings(s,n):
    poop = 0
    toop = 0
    for t in s:
        for o in n:
            if t == o:
                poop += 1
    if len(s) == len(n) == poop:
        return True
    else:
        return False

print(equal_strings("nlodve", "envold"))