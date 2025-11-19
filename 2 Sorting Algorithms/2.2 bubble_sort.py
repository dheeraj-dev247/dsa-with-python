def bubble_sort(nums):
    n = len(nums)
    for i in range(n - 2, -1, -1):
        for j in range(0, i + 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums  # Not required as we are doing in place


print(bubble_sort([3, 4, 5, 3, 2, 1]))
