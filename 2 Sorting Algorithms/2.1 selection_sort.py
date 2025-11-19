# Question Link:
# https://www.geeksforgeeks.org/problems/selection-sort/1


# Refer to the link below for detailed understanding:
# https://codeanddebug.in/blog/python-program-for-selection-sort-algorithm/


def selection_sort(nums):
    n = len(nums)
    for i in range(0, n):
        min_index = i
        for j in range(i + 1, n):
            if nums[j] < nums[min_index]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]
    return nums


print(selection_sort([4, 1, 3, 9, 7]))
