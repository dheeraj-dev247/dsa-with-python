# Better but not optimal here we are using 2 loops


def find_largest_and_second_largest(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:
        if num > largest:
            largest = num
    for num in nums:
        if num > second_largest and num != largest:
            second_largest = num

    return second_largest


# print(find_largest_and_second_largest([1, 2, 3, 41, 5]))


def find_largest_and_second_largest1(nums):
    largest = float("-inf")
    second_largest = float("-inf")

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


print(find_largest_and_second_largest1([1, 2, 3, 41, 5]))
