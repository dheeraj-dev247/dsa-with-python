def find_second_largest(nums):
    n = len(nums)
    largest = float("-inf")
    second_largest = float("-inf")
    for i in range(0, n):
        if nums[i] >= largest:
            second_largest = largest
            largest = nums[i]

    for i in range(0, n):
        if nums[i] >= second_largest and nums[i] != largest:
            second_largest = nums[i]

    return second_largest


print(find_second_largest([4, 5, 3, 6, 7]))
