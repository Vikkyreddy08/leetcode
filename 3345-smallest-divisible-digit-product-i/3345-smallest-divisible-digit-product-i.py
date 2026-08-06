class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            product=1
            num=n
            while num>0:
                last=num%10
                product*=last
                num//=10
            if product % t==0:
                return n
            n+=1