from typing import List
from math import gcd


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:

        n = len(coins)

        def lcm(a, b):
            return a // gcd(a, b) * b

        def count(x):
            total = 0

            for mask in range(1, 1 << n):
                current_lcm = 1
                bits = 0

                for i in range(n):
                    if mask & (1 << i):
                        current_lcm = lcm(current_lcm, coins[i])
                        bits += 1

                        # If LCM is greater than x,
                        # it contributes 0 multiples.
                        if current_lcm > x:
                            break

                if current_lcm > x:
                    continue

                multiples = x // current_lcm

                if bits % 2 == 1:
                    total += multiples
                else:
                    total -= multiples

            return total

        left = 1
        right = min(coins) * k

        while left < right:
            mid = (left + right) // 2

            if count(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left