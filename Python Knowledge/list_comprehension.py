#List comprehension is a concise way of creating lists in Python. It allows you to create a new list by applying an expression to each element of an existing iterable 
#(e.g., another list, tuple, or range), while also optionally filtering the elements based on a condition.

##[expression for item in iterable if condition]


#Traditional way
def test(all_handles):
    m = 0    
    for audience_size in all_handles:
            m += len(audience_size)

#Using list comphrension
def test(all_handles):
    m = sum(len(audience_size) for audience_size in all_handles)
