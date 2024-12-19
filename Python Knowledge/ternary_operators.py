
#Ternary operators are like list comprehensions.

## <expression1> if <condition> else <expression2>

#Traditional way
def number():
    if number % 2 == 0:
        is_even = True
    else:
        is_even = False
        
#Ternary operator way
def number():
    is_even = True if number % 2 == 0 else False