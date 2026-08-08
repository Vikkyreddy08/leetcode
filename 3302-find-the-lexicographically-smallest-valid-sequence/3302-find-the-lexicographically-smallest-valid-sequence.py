class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        # suf[j] = earliest index in word1 from which
        # word2[j:] can be matched exactly
        suf = [n] * (m + 1)

        i = n - 1

        for j in range(m - 1, -1, -1):
            while i >= 0 and word1[i] != word2[j]:
                i -= 1

            if i < 0:
                break

            suf[j] = i
            i -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            # Characters already match
            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            # Use our one allowed change
            elif not changed:
                # Remaining word2 must be matched exactly
                if j + 1 == m or (
                    suf[j + 1] < n and suf[j + 1] > i
                ):
                    ans.append(i)
                    j += 1
                    changed = True

        return ans if len(ans) == m else []