class Solution:
    def checkOverlap(self, radius, xCenter, yCenter, x1, y1, x2, y2):
        closest_x = max(x1, min(xCenter, x2))
        closest_y = max(y1, min(yCenter, y2))

        distance = (xCenter - closest_x) ** 2 + (yCenter - closest_y) ** 2

        return distance <= radius ** 2