class Solution:
    def maxNumberOfFamilies(self, n, reservedSeats):
        # Store reserved seats for each row
        rows = {}

        for row, seat in reservedSeats:
            # We only care about seats 2 to 9
            if 2 <= seat <= 9:
                rows.setdefault(row, set()).add(seat)

        # Assume every row is empty.
        # Every empty row can accommodate 2 groups.
        answer = 2 * n

        for seats in rows.values():

            # Check left block: 2,3,4,5
            left = all(seat not in seats for seat in [2, 3, 4, 5])

            # Check middle block: 4,5,6,7
            middle = all(seat not in seats for seat in [4, 5, 6, 7])

            # Check right block: 6,7,8,9
            right = all(seat not in seats for seat in [6, 7, 8, 9])

            # This row was initially counted as 2 groups.
            # Replace that count with the actual number possible.
            if left and right:
                groups = 2
            elif left or middle or right:
                groups = 1
            else:
                groups = 0

            answer -= 2
            answer += groups

        return answer