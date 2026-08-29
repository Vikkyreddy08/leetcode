class Solution:
    def lexicographicallySmallestArray(self, nums, limit):
        n = len(nums)

        # (value, original_index)
        arr = sorted((value, i) for i, value in enumerate(nums))

        result = nums[:]

        start = 0

        while start < n:
            end = start

            # Find one connected group
            while end + 1 < n and arr[end + 1][0] - arr[end][0] <= limit:
                end += 1

            # Values in this group
            values = [arr[i][0] for i in range(start, end + 1)]

            # Original indices in this group
            indices = [arr[i][1] for i in range(start, end + 1)]

            # Put smallest values at smallest indices
            indices.sort()

            for i, index in enumerate(indices):
                result[index] = values[i]

            start = end + 1

        return result