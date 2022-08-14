

from cmath import sqrt
from distutils.util import split_quoted


def divide_or_square(n):
    if n % 5 == 0:
        return sqrt(n)
    else:
        return n % 5 

print(divide_or_square(14))