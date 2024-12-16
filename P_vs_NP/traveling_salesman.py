#Traveling Salesman - Problem BigO[n!]
def tsp(cities, paths, dist):
    perms = permutations(cities)
    for perm in perms:
        total_dist = 0
        for i in range(1, len(perm)):
            total_dist += paths[perm[i - 1]][perm[i]]
        if total_dist < dist:
            return True
    return False  
            
# don't touch below this line

def permutations(arr):
    res = []
    res = helper(res, arr, len(arr))
    return res


def helper(res, arr, n):
    if n == 1:
        tmp = arr.copy()
        res.append(tmp)
    else:
        for i in range(n):
            res = helper(res, arr, n - 1)
            if n % 2 == 1:
                arr[n - 1], arr[i] = arr[i], arr[n - 1]
            else:
                arr[0], arr[n - 1] = arr[n - 1], arr[0]
    return res

#Traveling Salesman - Verify BigO[n]
def verify_tsp(paths, dist, actual_path):
    total_dist = 0
    for city in range(1, len(actual_path)):
        total_dist += paths[actual_path[city - 1]][actual_path[city]]
    if total_dist < dist:
        return True
    return False