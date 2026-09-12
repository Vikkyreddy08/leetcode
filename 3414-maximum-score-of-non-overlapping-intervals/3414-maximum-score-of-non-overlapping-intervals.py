from bisect import bisect_right
from typing import List


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        n = len(intervals)

        # [left, right, weight, original_index]
        arr = [
            [l, r, w, i]
            for i, (l, r, w) in enumerate(intervals)
        ]

        # Sort by left endpoint
        arr.sort()

        starts = [x[0] for x in arr]

        # next_idx[i] = first interval whose left > arr[i].right
        next_idx = [0] * n

        for i in range(n):
            next_idx[i] = bisect_right(starts, arr[i][1])

        # dp[k][i] = (maximum score, lexicographically smallest indices)
        # using at most k intervals from i onward
        dp = [
            [(0, []) for _ in range(n + 1)]
            for _ in range(5)
        ]

        for k in range(1, 5):

            for i in range(n - 1, -1, -1):

                # -------------------------
                # Option 1: Skip interval i
                # -------------------------
                skip_score, skip_indices = dp[k][i + 1]

                # -------------------------
                # Option 2: Take interval i
                # -------------------------
                j = next_idx[i]

                take_score = arr[i][2]

                take_indices = [arr[i][3]]

                # Add the best solution after this interval
                if j <= n:
                    next_score, next_indices = dp[k - 1][j]

                    take_score += next_score
                    take_indices += next_indices

                # IMPORTANT:
                # The final answer is compared using sorted
                # original indices.
                take_indices.sort()

                # -------------------------
                # Choose the better option
                # -------------------------
                if take_score > skip_score:

                    dp[k][i] = (
                        take_score,
                        take_indices
                    )

                elif take_score < skip_score:

                    dp[k][i] = (
                        skip_score,
                        skip_indices
                    )

                else:
                    # Same score:
                    # choose lexicographically smaller indices
                    if take_indices < skip_indices:
                        dp[k][i] = (
                            take_score,
                            take_indices
                        )
                    else:
                        dp[k][i] = (
                            skip_score,
                            skip_indices
                        )

        return dp[4][0][1]