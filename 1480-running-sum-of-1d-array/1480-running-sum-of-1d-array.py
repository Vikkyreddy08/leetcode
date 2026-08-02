class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        running=[0]*n

        for i in range(n):
            running[i] = running[i-1] + nums[i]
        return running
        