class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        # If there's only one element, it's trivially uniform
        if len(nums1) == 1:
            return True
        
        # Check if all are even or all are odd
        all_even = all(x % 2 == 0 for x in nums1)
        all_odd = all(x % 2 == 1 for x in nums1)
        
        if all_even or all_odd:
            return True
        
        # If mixed, we can always construct uniform parity using differences
        return True
