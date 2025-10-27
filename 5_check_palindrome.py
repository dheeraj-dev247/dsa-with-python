def check_palindrome(n):
    num = n
    rev_num = 0
    while num > 0:
        last_digit = num % 10
        rev_num = (rev_num * 10) + last_digit
        num = int(num / 10)

    return True if rev_num == n else False


print(check_palindrome(12))
