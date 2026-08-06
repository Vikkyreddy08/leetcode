class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)

        ans = [0] * n

        left = 0
        right = n - 1
        pos = n - 1

        while left <= right:

            if nums[left] ** 2 > nums[right] ** 2:
                ans[pos] = nums[left] ** 2
                left += 1
            else:
                ans[pos] = nums[right] ** 2
                right -= 1

            pos -= 1

        return ans