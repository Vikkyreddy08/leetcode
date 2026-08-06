class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        slow = 0

        # Move all non-zero elements to the front
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        # Fill remaining positions with zeros
        while slow < len(nums):
            nums[slow] = 0
            slow += 1