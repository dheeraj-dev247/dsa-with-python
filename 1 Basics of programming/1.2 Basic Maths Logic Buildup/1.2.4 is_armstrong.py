def is_armstrong(num):
    n = num
    total = 0
    while n > 0:
        last_digit = n%10
        total = total + (last_digit**3)
        n = n//10
    return True if total == num else False

print(is_armstrong(153))