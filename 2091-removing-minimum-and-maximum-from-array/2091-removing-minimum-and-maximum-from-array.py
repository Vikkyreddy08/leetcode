class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_idx = nums.index(min(nums))
        max_idx = nums.index(max(nums))

        left = min(min_idx, max_idx)
        right = max(min_idx, max_idx)

        # 1. Remove both from the front
        front = right + 1

        # 2. Remove both from the back
        back = n - left

        # 3. Remove one from front and one from back
        both = (left + 1) + (n - right)

        return min(front, back, both)