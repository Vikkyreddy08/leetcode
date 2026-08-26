class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        left = 0
        ones = 0

        min_len = float('inf')
        ans = ""

        for right in range(len(s)):
            if s[right] == '1':
                ones += 1

            # If ones become greater than k, shrink the window
            while ones > k:
                if s[left] == '1':
                    ones -= 1
                left += 1

            # When we have exactly k ones
            if ones == k:
                # Remove unnecessary leading zeros
                while s[left] == '0':
                    left += 1

                candidate = s[left:right + 1]
                length = len(candidate)

                if length < min_len:
                    min_len = length
                    ans = candidate

                elif length == min_len and candidate < ans:
                    ans = candidate

        return ans