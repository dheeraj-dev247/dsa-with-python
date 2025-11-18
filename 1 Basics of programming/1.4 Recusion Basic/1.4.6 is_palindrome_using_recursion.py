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
