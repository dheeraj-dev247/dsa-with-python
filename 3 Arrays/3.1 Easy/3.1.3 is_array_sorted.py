# Problem Link for this question:
# https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1


# Refer the article below for better understanding:
# https://codeanddebug.in/blog/check-if-array-is-sorted/


def is_array_sorted(nums):
    n = len(nums)
    for i in range(0, n - 1):
        if nums[i] > nums[i + 1]:
            return False
    return True


print(is_array_sorted([10, 20, 20, 40, 20]))
print(is_array_sorted([10, 20, 30, 40, 50]))
