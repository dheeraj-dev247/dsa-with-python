def rev_digit(num):
    while num >0:
        last_digit = num%10
        print("last_digit : ",last_digit)
        num = num//10
        return "Completed"


# print(rev_digit(345))

def count_digits(num):
    counts = 0
    while num > 0:
        counts += 1
        num = num//10
    return counts
    
# print(count_digits(1234567890))

def rev_integer(num):
    rev_int = 0
    while num > 0:
        last_digit = num%10
        rev_int = (rev_int * 10)+last_digit
        num = num//10
    return rev_int

# print(rev_integer(12345))

def is_palindrome(num):
    n = num
    rev = 0
    while n>0:
        ld = n%10
        rev = (rev*10)+ld
        n = n//10
    
    return True if rev==num else False

# print(is_palindrome(12211))


def is_armstrong(num):
    result = 0
    n = num
    while n > 0:
        ld = n%10
        result = result + ld**3
        n = n//10
    return True if num==result else False

print(is_armstrong(12))


