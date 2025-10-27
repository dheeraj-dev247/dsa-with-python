def countDigit(n):

    count = 0
    while n > 0:
        n = int(n / 10)
        count += 1
    return count


print(countDigit(56))
