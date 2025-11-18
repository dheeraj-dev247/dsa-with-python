# Solution 1 is done using while loop
class Solution:
    def isPalindrome(self, s):
        length = len(s)
        left = 0
        right = length - 1
        result = True
        while left <= right:
            if s[left] != s[right]:
                result = False
                break
            left += 1
            right -= 1
        return result


# s1 = Solution()
# print(s1.isPalindrome("wbklpwm"))


class Solution2:
    def is_palindrome(self, s):
        return self.solve(s, 0, len(s) - 1)

    def solve(self, s, l, r):
        # Base condition
        if l > r:
            return True
        if s[l] != s[r]:
            return False
        return self.solve(s, l + 1, r - 1)


s2 = Solution2()
print(s2.is_palindrome("wbklpwm"))
