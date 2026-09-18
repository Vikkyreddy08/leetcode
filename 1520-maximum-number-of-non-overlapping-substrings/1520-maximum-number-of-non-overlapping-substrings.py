class Solution:
    def maxNumOfSubstrings(self, s: str):
        n = len(s)

        first = [n] * 26
        last = [-1] * 26

        # Find first and last occurrence of every character
        for i, ch in enumerate(s):
            c = ord(ch) - ord('a')
            first[c] = min(first[c], i)
            last[c] = i

        intervals = []

        # Try creating a valid interval starting at
        # the first occurrence of each character
        for c in range(26):
            if first[c] == n:
                continue

            left = first[c]
            right = last[c]

            j = left
            valid = True

            while j <= right:
                x = ord(s[j]) - ord('a')

                # This character appeared before our interval
                if first[x] < left:
                    valid = False
                    break

                # We must include ALL occurrences of this character
                right = max(right, last[x])

                j += 1

            if valid:
                intervals.append((left, right))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        ans = []
        prev_end = -1

        for left, right in intervals:
            if left > prev_end:
                ans.append(s[left:right + 1])
                prev_end = right

        return ans