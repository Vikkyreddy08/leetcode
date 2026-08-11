class Solution:
    def missingInteger(self, nums):
        total = nums[0]

        # Find longest sequential prefix
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                total += nums[i]
            else:
                break

        # Find smallest missing integer >= total
        x = total

        while x in nums:
            x += 1

        return x