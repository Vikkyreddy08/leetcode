class Solution:
    def largestOverlap(self, img1, img2):
        points1 = []
        points2 = []

        n = len(img1)

        # Store coordinates of 1s
        for r in range(n):
            for c in range(n):
                if img1[r][c] == 1:
                    points1.append((r, c))

                if img2[r][c] == 1:
                    points2.append((r, c))

        count = {}
        answer = 0

        # Compare every 1 from img1 with every 1 from img2
        for r1, c1 in points1:
            for r2, c2 in points2:

                dr = r2 - r1
                dc = c2 - c1

                count[(dr, dc)] = count.get((dr, dc), 0) + 1

                answer = max(answer, count[(dr, dc)])

        return answer