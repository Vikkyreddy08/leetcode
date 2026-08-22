class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sum=0
        product=1
        orginal=n
        while n>0:
            digit=n%10
            sum=sum+digit
            product*=digit
            n//=10
        if orginal % (sum+product)==0:
            return True
        return False
        


        