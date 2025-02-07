def factorial_r(x):
    fact = 1
    
    if x == 0:
        return 1

    for i in range(1, x+1):
        fact = fact * i

    return fact