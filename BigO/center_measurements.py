# Median
def calculate_median(lst):
    # Step 1: Sort the list
    sorted_lst = sorted(lst)

    # Step 2: Calculate the median
    n = len(sorted_lst)
    
    if n % 2 == 1:
        # If the length is odd, return the middle element
        median = sorted_lst[n // 2]
    else:
        # If the length is even, return the average of the two middle elements
        middle1 = sorted_lst[(n // 2) - 1]
        middle2 = sorted_lst[n // 2]
        median = (middle1 + middle2) / 2