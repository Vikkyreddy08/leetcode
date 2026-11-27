
from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        free = [0] * n

        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    free[i] += 1

        min_price = min(price for factor, price in items)

        dp = [-1] * (budget + 1)
        dp[0] = 0

        for i in range(n):
            price = items[i][1]

            for b in range(budget, price - 1, -1):
                if dp[b - price] != -1:
                    dp[b] = max(
                        dp[b],
                        dp[b - price] + free[i] + 1
                    )

        ans = 0

        for spent in range(budget + 1):
            if dp[spent] != -1:
                ans = max(
                    ans,
                    dp[spent] + (budget - spent) // min_price
                )

        return ans
