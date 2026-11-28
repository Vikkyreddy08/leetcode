
class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        # Step 1: Find minimum price and count factors
        freq = [0] * (n + 1)
        min_price = float('inf')

        for factor, price in items:
            freq[factor] += 1
            min_price = min(min_price, price)

        # Step 2: Calculate gain for every factor
        gain = [0] * (n + 1)

        for f in range(1, n + 1):
            if freq[f] == 0:
                continue

            count = 0

            for multiple in range(f, n + 1, f):
                count += freq[multiple]

            gain[f] = count - 1

        # Step 3: Sort items by price
        items.sort(key=lambda x: x[1])

        answer = 0

        # Step 4: Buy profitable boosted copies
        for factor, price in items:

            if price >= 2 * min_price:
                break

            if gain[factor] == 0:
                continue

            buy = min(gain[factor], budget // price)

            answer += 2 * buy
            budget -= buy * price

        # Step 5: Buy normal copies using remaining budget
        answer += budget // min_price

        return answer
