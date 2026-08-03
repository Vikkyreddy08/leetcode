class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(1,n):
            nums[i]+=nums[i-1]
        total=nums[-1]
        for i in range(n):
            if i==0:
                left=0
            else:
                left=nums[i-1]

            right=total-nums[i]
            
            if left==right:
                return i
            
        return -1
            


        