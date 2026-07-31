class Solution:
    def minimumPushes(self, word):
        freq = [0] * 26

        for ch in word:
            freq[ord(ch) - ord('a')] += 1

        freq.sort(reverse=True)

        ans = 0

        for i, f in enumerate(freq):
            if f == 0:
                break
            ans += f * (i // 8 + 1)

        return ans