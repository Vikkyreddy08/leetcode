class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sumdigit=0
        product=1
        orginal=n
        while n>0:
            digit=n%10
            sumdigit+=+digit
            product*=digit
            n//=10
        if orginal % (sumdigit+product)==0:
            return True
        return False
        


        