
def biggest_odd(n):
    lice = [x for x in n if int(x) % 2 != 0 and int(x) > 2 ]
    return sorted(lice[-1]) 
  

print(*biggest_odd("23569"))

