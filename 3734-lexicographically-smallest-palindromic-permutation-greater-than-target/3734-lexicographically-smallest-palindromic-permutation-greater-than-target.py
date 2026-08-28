from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        count = Counter(s)

        # More than one odd frequency -> no palindrome possible
        odd = []

        for ch in count:
            if count[ch] % 2 == 1:
                odd.append(ch)

        if len(odd) > 1:
            return ""

        middle = odd[0] if odd else ""

        # Build available characters for the first half
        half_count = [0] * 26

        for ch, freq in count.items():
            half_count[ord(ch) - ord('a')] = freq // 2

        m = len(s) // 2
        target_half = target[:m]

        result = []
        greater = False

        # Build the smallest possible half >= target's first half
        for i in range(m):
            target_char = ord(target_half[i]) - ord('a')

            if greater:
                # Already greater, use smallest available character
                for c in range(26):
                    if half_count[c] > 0:
                        result.append(chr(c + ord('a')))
                        half_count[c] -= 1
                        break
            else:
                # Try to use the same character
                if half_count[target_char] > 0:
                    result.append(chr(target_char + ord('a')))
                    half_count[target_char] -= 1
                else:
                    # Need a larger available character
                    found = False

                    for c in range(target_char + 1, 26):
                        if half_count[c] > 0:
                            result.append(chr(c + ord('a')))
                            half_count[c] -= 1
                            greater = True
                            found = True
                            break

                    # Cannot continue; backtrack
                    if not found:
                        while result:
                            last = ord(result.pop()) - ord('a')
                            half_count[last] += 1

                            for c in range(last + 1, 26):
                                if half_count[c] > 0:
                                    result.append(chr(c + ord('a')))
                                    half_count[c] -= 1
                                    greater = True
                                    found = True
                                    break

                            if found:
                                break

                        if not found:
                            return ""

        half = ''.join(result)

        # Fill remaining characters in sorted order
        remaining = []

        for c in range(26):
            remaining.extend(chr(c + ord('a')) * half_count[c])

        half += ''.join(remaining)

        palindrome = half + middle + half[::-1]

        # If equal or smaller, get next permutation
        if palindrome <= target:
            arr = list(half)

            i = len(arr) - 2

            while i >= 0 and arr[i] >= arr[i + 1]:
                i -= 1

            if i < 0:
                return ""

            j = len(arr) - 1

            while arr[j] <= arr[i]:
                j -= 1

            arr[i], arr[j] = arr[j], arr[i]
            arr[i + 1:] = reversed(arr[i + 1:])

            half = ''.join(arr)
            palindrome = half + middle + half[::-1]

        return palindrome if palindrome > target else ""