class Solution(object):
    
    def twoSum(self, nums, target):
       dic={}
       for i,num in enumerate(nums): 
        compliment=target-num
        if compliment in dic:
            return dic[compliment],i
        dic[num]=i


 
        