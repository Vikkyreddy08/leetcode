class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        window = 0
        minimum = float('inf')

        for right in range(len(nums)):
            window += nums[right]

            while window >= target:
                minimum = min(minimum, right - left + 1)

                window -= nums[left]
                left += 1

        return 0 if minimum == float('inf') else minimum