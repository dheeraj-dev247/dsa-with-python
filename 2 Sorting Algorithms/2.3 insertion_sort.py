# Question Link:
# https://www.geeksforgeeks.org/problems/insertion-sort/0


# Refer to the link below for detailed understanding:
# https://codeanddebug.in/blog/insertion-sort-algorithm-explained-in-python/


def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


print(insertion_sort([3, 4, 5, 2, 1]))
