class Solution(object):
    def maxProduct(self, nums):
        largest = float("-inf")
        second = float("-inf")

        for num in nums:
            if num > largest:
                second = largest
                largest = num
            elif num > second:
                second = num

        return (largest - 1) * (second - 1)