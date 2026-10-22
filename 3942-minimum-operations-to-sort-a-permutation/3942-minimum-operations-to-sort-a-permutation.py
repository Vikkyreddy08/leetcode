class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        pos = nums.index(0)

        # Check ascending circular order
        if all(nums[(i + 1) % n] == (nums[i] + 1) % n
               for i in range(n)):
            return min(pos, n - pos + 2)

        # Check descending circular order
        if all(nums[(i + 1) % n] == (nums[i] - 1) % n
               for i in range(n)):
            k = (n - 1 - pos) % n
            return 1 + min(k, n - k)

        return -1