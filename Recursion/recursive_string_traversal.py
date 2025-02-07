def reverse_string(s):
    if len(s) == 0:
        return ""
    result = s[-1] + reverse_string(s[:-1])
    return result