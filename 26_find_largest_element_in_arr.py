def largest(arr):
    maximum = arr[0]
    for num in arr:
        maximum = max(maximum, num)
    return maximum


print(largest([-111, -88, -777, -56, -90]))
