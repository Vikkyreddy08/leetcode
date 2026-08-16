class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        count = [0, 0, 0]

        for stone in stones:
            count[stone % 3] += 1

        # If there are no remainder-1 or remainder-2 stones,
        # Alice cannot avoid losing.
        if count[1] == 0 and count[2] == 0:
            return False

        # If there are many 0-remainder stones, they can be
        # used to change whose turn it is.
        if count[0] % 2 == 1:
            return abs(count[1] - count[2]) > 2
        else:
            return count[1] > 0 and count[2] > 0