#Big O(n) - Order "N" [LINEAR]
def find_max(nums):
    max_so_far = float("-inf")

    for num in nums:
        if num > max_so_far:
            max_so_far = num
    return max_so_far


#Big O(n^2) - Order N Squared [SQUARED]
def does_name_exist(first_names, last_names, full_name):
    government_name = []

    for name1 in first_names:    
        for name2 in last_names:
            government_name = (name1 + ' ' + name2)
            if government_name == full_name:
                return True
    return False
        
#Big O(nm) - [Order N] *For Two Inputs / Common w/ List of Lists
def get_avg_brand_followers(all_handles, brand_name):
    count = 0
    for handles in all_handles:
        for handle in handles:
            if brand_name in handle:
                count += 1
    return count / len(all_handles)

#Big O(1) - Order 1 [CONSTANT]
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None
    
#Big O(log(n)) - Order Log N [INVERSE SQUARED]
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    median = 0

    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
    
            
        
    
