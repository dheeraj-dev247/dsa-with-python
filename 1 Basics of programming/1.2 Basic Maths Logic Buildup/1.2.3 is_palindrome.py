def isPalindrome(num):
    n = num
    rev_num = 0
    while n > 0:
        last_digit = n%10
        rev_num = (rev_num * 10) + last_digit
        n = n//10
    return True if rev_num == num else False

print(isPalindrome(121))