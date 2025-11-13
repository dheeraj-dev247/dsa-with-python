def count_digits(num):
    n = abs(num)
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count +=1
        n = n//10
    return count

print(count_digits(12345))