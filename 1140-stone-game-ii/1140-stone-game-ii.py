from functools import lru_cache

class Solution:
    def stoneGameII(self, piles):
        n = len(piles)

        # suffix[i] = sum of piles from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = piles[i] + suffix[i + 1]

        @lru_cache(None)
        def dp(i, M):
            # Can take all remaining piles
            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            for X in range(1, 2 * M + 1):
                # Stones current player takes
                taken = suffix[i] - suffix[i + X]

                # Opponent's best score
                opponent = dp(i + X, max(M, X))

                # Current player's total
                current = taken + suffix[i + X] - opponent

                best = max(best, current)

            return best

        return dp(0, 1)