def isPalindrome1(str):
    rev_str = ""
    for char in str:
        rev_str = char + rev_str
    return rev_str == str


# print(isPalindrome1("moma"))


def isPalindrome2(str):
    n = len(str)
    left = 0
    right = n - 1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True


# print(isPalindrome2("mom"))


def isPalindrome_using_rec(str, left, right):
    if left >= right:
        return True
    if str[left] != str[right]:
        return False
    return isPalindrome_using_rec(str, left + 1, right - 1)


print(isPalindrome_using_rec("madam", 0, len("madam") - 1))
