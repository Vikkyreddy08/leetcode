class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        window = 0
        maximum=float('-inf')

        for right in range(len(nums)):
            window += nums[right]

            if right - left + 1 == k:
                maximum=max(window,maximum)
                # use window
                window -= nums[left]
                left += 1
        return maximum/k