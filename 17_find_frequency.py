def findFreq(arr, x):
    hash_map = {}
    for item in arr:
        hash_map[item] = hash_map.get(item, 0) + 1
    return hash_map.get(x, 0)


print(findFreq([1, 2, 3, 3, 2, 1], 4))
