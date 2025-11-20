# Problem link for this question:
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Refer the article below for better understanding:
# https://codeanddebug.in/blog/remove-duplicates-from-sorted-array-leetcode-26/


def remove_duplicates_from_array_brute_force(nums):
    n = len(nums)
    freq_map = {}
    for i in range(0, n):
        freq_map[nums[i]] = 0

    j = 0
    for key in freq_map:
        nums[j] = key
        j += 1
    return j


def remove_duplicates_from_array_optimal(nums):
    n = len(nums)
    i = 0
    j = i + 1
    while j < n:
        if nums[j] != nums[i]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i + 1


print(remove_duplicates_from_array_brute_force([1, 1, 1, 2, 3, 4, 5, 5, 5, 6]))
print(remove_duplicates_from_array_optimal([1, 1, 1, 2, 3, 4, 5, 5, 5, 6]))
