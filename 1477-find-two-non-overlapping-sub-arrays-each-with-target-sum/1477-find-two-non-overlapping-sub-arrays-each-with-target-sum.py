class Solution:
    def minSumOfLengths(self, arr, target):
        n = len(arr)
        INF = n + 1

        # best[i] = shortest target-sum subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        curr_sum = 0
        answer = INF
        shortest = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Check for a previous non-overlapping subarray
                if left > 0 and best[left - 1] != INF:
                    answer = min(answer, length + best[left - 1])

                shortest = min(shortest, length)

            best[right] = shortest

        return -1 if answer == INF else answer