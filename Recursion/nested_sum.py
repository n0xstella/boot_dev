def sum_nested_list(lst):
    current_sum = 0

    for item in lst:
        if isinstance(item, int):
            current_sum += item
        if isinstance(item, list):
            new_sum = sum_nested_list(item)
            current_sum += new_sum
    
    return current_sum
