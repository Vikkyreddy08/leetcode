class Solution(object):
    def smallestPalindrome(self, s):
        freq = [0] * 26

        # Count frequency
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        left = []
        middle = ""

        # Build left half
        for i in range(26):
            if freq[i] % 2 == 1:
                middle = chr(i + ord('a'))

            left.append(chr(i + ord('a')) * (freq[i] // 2))

        left = "".join(left)

        return left + middle + left[::-1]