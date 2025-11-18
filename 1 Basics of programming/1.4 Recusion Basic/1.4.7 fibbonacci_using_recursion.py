class Solution:
    def fib(self, n):
        return self._helper(n)

    def _helper(self, n):
        # Base condition
        if n == 0 or n == 1:
            return n
        return self._helper(n - 1) + self._helper(n - 2)


s = Solution()
print(s.fib(4))
