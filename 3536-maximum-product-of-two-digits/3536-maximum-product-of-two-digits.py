class Solution(object):
    def maxProduct(self, n):
        first=0
        second=0
        while n>0:
            digits=n%10
            n//=10
            if digits>first:
                second=first
                first=digits
            elif digits>second:
                second=digits
        return first*second



            




        

        