import math


def prime_factors(n):
    prime_factors_lst = []

    while n % 2 == 0:
        n /= 2
        prime_factors_lst.append(2)   
    for factor in range(3, int(math.sqrt(n)) + 1, 2):
        while n % factor == 0:
            n /= factor
            prime_factors_lst.append(factor)

    if n > 2:
        prime_factors_lst.append(n)

    return prime_factors_lst