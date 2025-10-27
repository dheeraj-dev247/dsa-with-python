def is_armstrong(n):
    num = n
    total = 0
    while num > 0:
        last_digit = num % 10
        total = (last_digit**3) + total
        num = int(num / 10)
    return n == total


print(is_armstrong(121))
print(is_armstrong(153))
