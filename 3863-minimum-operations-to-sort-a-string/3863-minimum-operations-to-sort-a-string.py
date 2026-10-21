class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if s == ''.join(sorted(s)):
            return 0

        if n == 2:
            return -1

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        if s[0] > max(s[1:]) and s[-1] < min(s[:-1]):
            return 3

        return 2