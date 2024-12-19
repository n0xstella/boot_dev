#Sorted function - O(1) [CONSTANT]
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"

def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies
    

def vanity_sort(influencers):
    return sorted(influencers, key=vanity)

#Bubble sorting
def bubble_sort(nums):
    n = len(nums)

    for i in range(n):
        for j in range(0, n-i-1):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#Merge Sort - O(n*log(n)) [LINEARRITHMIC]
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    else:
        midpoint = len(nums) // 2
        first_half = merge_sort(nums[:midpoint])
        second_half = merge_sort(nums[midpoint:])
        return merge(first_half, second_half)
        
def merge(first, second):
    merged = []
    i = j = 0

    if not isinstance(first, list):
        first = [first]
    if not isinstance(second, list):
        second = [second]
    
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    
    merged.extend(first[i:])
    merged.extend(second[j:])
    
    return merged

## Alternate
def merge_sort(nums):
    if len(nums) < 2:
        return nums
    first = merge_sort(nums[: len(nums) // 2])
    second = merge_sort(nums[len(nums) // 2 :])
    return merge(first, second)


def merge(first, second):
    final = []
    i = 0
    j = 0
    while i < len(first) and j < len(second):
        if first[i] <= second[j]:
            final.append(first[i])
            i += 1
        else:
            final.append(second[j])
            j += 1
    while i < len(first):
        final.append(first[i])
        i += 1
    while j < len(second):
        final.append(second[j])
        j += 1
    return final

# Insertion Sort
def insertion_sort(nums):
    if not isinstance(nums, list):
        nums = [nums]
    
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
        
    return nums

## Alternate
def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j - 1] > nums[j]:
            temp = nums[j]
            nums[j] = nums[j - 1]
            nums[j - 1] = temp
            j -= 1
    return nums

#Quick Sort - O(n*log(n)) [LINEARRITHMIC]
def quick_sort(nums, low, high):
    if not isinstance(nums, list):
        return nums
        
    if low < high:
        pivot_index = partition(nums, low, high)
        quick_sort(nums, low, pivot_index - 1)
        quick_sort(nums, pivot_index + 1, high)
    return nums

def partition(nums, low, high):
    pivot = nums[high]
    i = low

    for j in range(low, high):
        if nums[j] < pivot:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
    nums[i], nums[high] = nums[high], nums[i]
    return i

#Selection Sort
def selection_sort(nums):
    if not isinstance(nums, list):
        return nums
            
    for i in range(len(nums)):
        smallest_idx = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
