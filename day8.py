def odd_even(n):
    n = sorted(n)
    for i in sorted(n, reverse=True):
        if i % 2 == 0:
            even = i 
            break
    for j in n:
        if j % 2 != 0:
            odd = j
            break
    
    return i - j


print(odd_even([1,2,4,6]))