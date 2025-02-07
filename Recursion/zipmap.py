"""
It takes two lists as input and returns a dictionary where the first list provides the keys and the second list provides the values.

If either the keys or values list is empty, returns an empty dictionary (base case).
Recursively call zipmap on all but the first elements from keys and values.
Adds the first element of keys to the resulting dictionary, and set its value to the first element in values.
Return the updated dictionary.
"""

def zipmap(keys, values):
    if not keys or not values:
        return {}
    
    result = zipmap(keys[1:], values[1:])
    return {keys[0]: values[0], **result}