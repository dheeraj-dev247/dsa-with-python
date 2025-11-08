def rotate_arr(num):
    n = len(num)
    # temp = num[n - 1]
    for i in range(n - 1, -1, -1):
        print(num[i])


print(rotate_arr([1, 2, 3, 4]))
