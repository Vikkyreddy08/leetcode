class Node:
    __slots__ = ("prod", "pref")

    def __init__(self, prod, pref):
        self.prod = prod
        self.pref = pref


class SegmentTree:
    def __init__(self, nums, k):
        self.n = len(nums)
        self.k = k

        # Store prod and pref directly in arrays
        self.prod = [1] * (4 * self.n)
        self.pref = [[0] * k for _ in range(4 * self.n)]

        self.build(1, 0, self.n - 1, nums)

    def build(self, node, left, right, nums):
        if left == right:
            r = nums[left] % self.k

            self.prod[node] = r
            self.pref[node][r] = 1

            return

        mid = (left + right) // 2

        self.build(node * 2, left, mid, nums)
        self.build(node * 2 + 1, mid + 1, right, nums)

        self.pull(node)

    def pull(self, node):
        left = node * 2
        right = left + 1

        left_prod = self.prod[left]

        # Product of complete segment
        self.prod[node] = (
            left_prod * self.prod[right]
        ) % self.k

        p = self.pref[node]
        lp = self.pref[left]
        rp = self.pref[right]

        # Reset
        for r in range(self.k):
            p[r] = lp[r]

        # Prefixes that use:
        # entire left + prefix of right
        for r in range(self.k):
            p[(left_prod * r) % self.k] += rp[r]

    def update(self, node, left, right, pos, value):
        if left == right:
            r = value % self.k

            self.prod[node] = r

            p = self.pref[node]

            for i in range(self.k):
                p[i] = 0

            p[r] = 1

            return

        mid = (left + right) // 2

        if pos <= mid:
            self.update(
                node * 2,
                left,
                mid,
                pos,
                value
            )
        else:
            self.update(
                node * 2 + 1,
                mid + 1,
                right,
                pos,
                value
            )

        self.pull(node)

    def query(self, node, left, right, ql, qr):
        # Complete segment
        if ql <= left and right <= qr:
            return self.prod[node], self.pref[node][:]

        mid = (left + right) // 2

        # Completely in left
        if qr <= mid:
            return self.query(
                node * 2,
                left,
                mid,
                ql,
                qr
            )

        # Completely in right
        if ql > mid:
            return self.query(
                node * 2 + 1,
                mid + 1,
                right,
                ql,
                qr
            )

        # Crosses middle
        left_prod, left_pref = self.query(
            node * 2,
            left,
            mid,
            ql,
            qr
        )

        right_prod, right_pref = self.query(
            node * 2 + 1,
            mid + 1,
            right,
            ql,
            qr
        )

        result_pref = left_pref

        for r in range(self.k):
            result_pref[
                (left_prod * r) % self.k
            ] += right_pref[r]

        result_prod = (
            left_prod * right_prod
        ) % self.k

        return result_prod, result_pref


class Solution:
    def resultArray(self, nums, k, queries):

        seg = SegmentTree(nums, k)

        n = len(nums)
        answer = []

        for index, value, start, x in queries:

            # Persistent update
            seg.update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # Query [start ... n-1]
            _, pref = seg.query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            # We need prefixes whose product % k == x
            answer.append(pref[x])

        return answer