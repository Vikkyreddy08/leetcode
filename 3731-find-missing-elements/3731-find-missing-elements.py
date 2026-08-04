class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s=set(nums)
        ans=[]
        left=min(nums)
        right=max(nums)
        for i in range(left,right+1):
            if i not in s:
                ans.append(i)
        return ans

        
            



        