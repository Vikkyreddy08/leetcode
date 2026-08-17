class Solution:
    def stoneGameV(self, stoneValue):
        n = len(stoneValue)

        # Prefix sums
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        # dp[l][r] = maximum score for subarray l...r
        dp = [[0] * n for _ in range(n)]

        # left_best[l][r]:
        # max of dp[l][k] + sum(l, k)
        # for k in [l, r-1]
        left_best = [[0] * n for _ in range(n)]

        # right_best[l][r]:
        # max of dp[k][r] + sum(k, r)
        # for k in [l+1, r]
        right_best = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):

            for l in range(n - length + 1):

                r = l + length - 1

                # Update left range maximum
                left_sum = prefix[r] - prefix[l]

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r - 1] + left_sum
                )

                # Update right range maximum
                right_sum = prefix[r + 1] - prefix[l + 1]

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l + 1][r] + right_sum
                )

                total = prefix[r + 1] - prefix[l]

                # Binary search for the last split
                # where left_sum <= right_sum
                low = l
                high = r - 1

                while low <= high:

                    mid = (low + high) // 2

                    left = prefix[mid + 1] - prefix[l]

                    if left * 2 <= total:
                        low = mid + 1
                    else:
                        high = mid - 1

                best = 0

                # Case 1:
                # left_sum <= right_sum
                #
                # high is the last such split.
                if high >= l:
                    best = max(
                        best,
                        left_best[l][high + 1]
                    )

                # Case 2:
                # left_sum > right_sum
                #
                # low is the first such split.
                if low <= r - 1:
                    best = max(
                        best,
                        right_best[low][r]
                    )

                # Case 3:
                # Exact equality.
                #
                # If high is an exact 50/50 split,
                # Alice can choose either side.
                if high >= l:

                    left = prefix[high + 1] - prefix[l]

                    if left * 2 == total:
                        best = max(
                            best,
                            right_best[high][r]
                        )

                dp[l][r] = best

        return dp[0][n - 1]