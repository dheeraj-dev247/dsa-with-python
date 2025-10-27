# There are 2 approach
# 1. brute force
# 2. dividing by half and add 1 + n


def countFactors(n):
    count = 0
    num = n
    for i in range(1, num + 1):
        if num % i == 0:
            count = count + 1
    return count


# print(countFactors(100))


def countFactors1(n):
    count = 0
    num = n
    half = num // 2
    for i in range(1, half + 1):
        if num % i == 0:
            count = count + 1
    return count + 1


# print(countFactors1(100))
