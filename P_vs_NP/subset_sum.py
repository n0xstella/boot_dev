# Correct Answer
def subset_sum(nums, target):
    return find_subset_sum(nums, target, len(sorted(nums, reverse=True)))
    

def find_subset_sum(nums, target, index):
    if target == 0:
        return True
    if index == 0 or target < 0:
        return False
    
    if nums[index - 1] > target:
        return find_subset_sum(nums, target, index - 1)
    else:
        return find_subset_sum(nums, target, index - 1) or find_subset_sum(nums, target - nums[index - 1], index - 1)
        

# Try 2
def find_subset_sum(nums, target, index):
    for index in range(len(nums)):
        if target == 0:
            return True
        if nums[index] < 0 and target != 0:
            return False
        if nums[index - 1] > target:
            return find_subset_sum(nums, target, index - 1)
        else:
            if find_subset_sum(nums, target, index - 1) or [
                find_subset_sum(nums, target - nums[index - 1], index - 1)
            ] == True:
                return True
    return False

def subset_sum(nums, target):
    return find_subset_sum(nums, target, sorted(nums, reverse=True))