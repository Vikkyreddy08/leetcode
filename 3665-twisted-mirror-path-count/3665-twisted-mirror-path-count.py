
from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7

        m, n = len(grid), len(grid[0])

        right = [[-1] * n for _ in range(m)]
        down = [[-1] * n for _ in range(m)]

        # Precompute mirror destinations
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):

                if grid[r][c] == 0:
                    idx = r * n + c
                    right[r][c] = idx
                    down[r][c] = idx

                else:
                    # Enter mirror moving right -> down
                    if r + 1 < m:
                        right[r][c] = down[r + 1][c]

                    # Enter mirror moving down -> right
                    if c + 1 < n:
                        down[r][c] = right[r][c + 1]

        # Dynamic Programming
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        for r in range(m):
            for c in range(n):

                ways = dp[r][c]

                if ways == 0:
                    continue

                # Move right
                if c + 1 < n:
                    dest = right[r][c + 1]

                    if dest != -1:
                        nr, nc = divmod(dest, n)
                        dp[nr][nc] = (
                            dp[nr][nc] + ways
                        ) % MOD

                # Move down
                if r + 1 < m:
                    dest = down[r + 1][c]

                    if dest != -1:
                        nr, nc = divmod(dest, n)
                        dp[nr][nc] = (
                            dp[nr][nc] + ways
                        ) % MOD

        return dp[m - 1][n - 1]
