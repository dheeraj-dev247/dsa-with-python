# Approach 1


def find_largest_brute_force(nums):
    largest = float("-inf")
    for number in nums:
        largest = max(largest, number)
    return largest


print(find_largest_brute_force([2, 4, 1, 3, 2, 33, 111, 1, 22]))
