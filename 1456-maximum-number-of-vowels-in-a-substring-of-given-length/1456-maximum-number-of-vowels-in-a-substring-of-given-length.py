class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        left = 0
        window = 0
        maximum = 0

        vowels = "aeiou"

        for right in range(len(s)):
            if s[right] in vowels:
                window += 1

            if right - left + 1 == k:
                maximum = max(maximum, window)

                if s[left] in vowels:
                    window -= 1

                left += 1

        return maximum