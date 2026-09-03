class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        mn = min(nums1)

        # If minimum is odd, we can make every number odd
        if mn % 2 == 1:
            return True

        # If minimum is even, every number must already be even
        for x in nums1:
            if x % 2 == 1:
                return False

        return True