def is_prime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print(is_prime(15))


def is_prime1(n):
    if n == 1:
        return False
    if n == 2:
        return True
    half = n // 2
    for i in range(2, half + 1):
        if n % i == 0:
            return False
    return True


print(is_prime1(15))
