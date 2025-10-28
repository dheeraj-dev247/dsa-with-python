def func(nums, left, right):
    if left == right or left > right:
        return
    nums[left], nums[right] = nums[right], nums[left]
    func(nums, left + 1, right - 1)


def rev_arr(nums, left, right):
    func(nums, left - 1, right - 1)
    return nums


print(rev_arr([1, 2, 3, 4, 5, 6, 7], 2, 4))
