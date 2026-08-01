class Solution:
    def predictTheWinner(self, nums):
        memo = {}

        def dp(left, right):
            if left == right:
                return nums[left]

            if (left, right) in memo:
                return memo[(left, right)]

            take_left = nums[left] - dp(left + 1, right)
            take_right = nums[right] - dp(left, right - 1)

            memo[(left, right)] = max(take_left, take_right)
            return memo[(left, right)]

        return dp(0, len(nums) - 1) >= 0