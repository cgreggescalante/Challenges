# Divisors of Binomial Product
from math import factorial

from Utilities.Factoring import divisors


def B(n):
    d = 1
    for i in range(1, n+1):
        d *= factorial(i)
    return int(factorial(n)**(n+1) / d**2)


def D(n):
    return sum(divisors(B(n)))


def S(n):
    print(sum(list(map(D, [k+1 for k in range(n)]))))


S(20000)
