def is_arr_sorted(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


print(is_arr_sorted([10, 20, 30, 40, 50]))
print(is_arr_sorted([90, 80, 100, 70, 40, 30]))
