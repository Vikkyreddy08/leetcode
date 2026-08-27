from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        count = Counter(s)
        result = []

        # Try matching target from left to right
        for i in range(len(s)):

            if count[target[i]] > 0:
                result.append(target[i])
                count[target[i]] -= 1

            else:
                # Find the smallest available character greater than target[i]
                for ch in range(ord(target[i]) + 1, ord('z') + 1):
                    c = chr(ch)

                    if count[c] > 0:
                        result.append(c)
                        count[c] -= 1

                        # Add remaining characters in sorted order
                        for letter in sorted(count):
                            result.append(letter * count[letter])

                        return ''.join(result)

                break

        # Backtrack from right to left
        while result:
            i = len(result) - 1

            last = result.pop()
            count[last] += 1

            # Find smallest character greater than target[i]
            for ch in range(ord(target[i]) + 1, ord('z') + 1):
                c = chr(ch)

                if count[c] > 0:
                    result.append(c)
                    count[c] -= 1

                    # Add remaining characters in sorted order
                    for letter in sorted(count):
                        result.append(letter * count[letter])

                    return ''.join(result)

        return ""