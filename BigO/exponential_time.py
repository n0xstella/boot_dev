import math

#Fibonnaci Sequence
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    grandp = 0
    parent = 1
    
    for i in range(2, n + 1):
        current = parent + grandp
        grandp = parent
        parent = current
    return current

#Big O(2^n)
def power_set(input_set):
    if len(input_set) == 0:
        return [[]]

    subsets = []
    first = input_set[0]
    remaining = input_set[1:]
    remaining_subsets = power_set(remaining)
    for subset in remaining_subsets:
        subsets.append([first] + subset)
        subsets.append(subset)
    return subsets
    
## Alt
def power_set(input_set):
    if not isinstance(input_set, list):
        return []
    elif not input_set:
        return [[]]
    else:
        final_list = []
        subset = power_set(input_set[1:])
        for s in subset:
            final_list.append([input_set[0]] + s)
            final_list.append(s)
        final_list.append(input_set[0])
        return final_list