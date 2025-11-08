def remove_duplicates(arr):
    freq_hashmap = {}
    n = len(arr)
    for i in range(0, n):
        freq_hashmap[arr[i]] = 0

    j = 0
    for k in freq_hashmap:
        arr[j] = k
        j += 1
    print(arr)
    return j


print(remove_duplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
