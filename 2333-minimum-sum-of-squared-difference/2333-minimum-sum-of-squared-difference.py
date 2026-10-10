class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int],
                         k1: int, k2: int) -> int:
        diffs = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diffs) <= k:
            return 0

        left, right = 0, max(diffs)

        while left < right:
            mid = (left + right) // 2
            operations = sum(max(d - mid, 0) for d in diffs)

            if operations <= k:
                right = mid
            else:
                left = mid + 1

        level = left
        used = sum(max(d - level, 0) for d in diffs)
        remaining = k - used

        ans = sum(min(d, level) ** 2 for d in diffs)
        ans -= remaining * (2 * level - 1)

        return ans