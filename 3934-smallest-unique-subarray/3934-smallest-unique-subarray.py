
class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 1

        # Coordinate compression
        vals = sorted(set(nums))
        mp = {v: i + 1 for i, v in enumerate(vals)}
        s = [mp[x] for x in nums]

        # Build suffix array using counting sort
        sa = list(range(n))
        rank = s[:]
        tmp = [0] * n
        sa2 = [0] * n

        k = 1
        max_rank = len(vals)

        def counting_sort(indices, key, size):
            cnt = [0] * (size + 1)

            for i in indices:
                cnt[key(i)] += 1

            total = 0
            for i in range(size + 1):
                c = cnt[i]
                cnt[i] = total
                total += c

            result = [0] * len(indices)

            for i in indices:
                v = key(i)
                result[cnt[v]] = i
                cnt[v] += 1

            return result

        while k < n:
            sa = counting_sort(
                sa,
                lambda i: rank[i + k] if i + k < n else 0,
                max_rank
            )

            sa = counting_sort(
                sa,
                lambda i: rank[i],
                max_rank
            )

            tmp[sa[0]] = 1
            new_rank = 1

            for j in range(1, n):
                a, b = sa[j - 1], sa[j]

                a2 = rank[a + k] if a + k < n else 0
                b2 = rank[b + k] if b + k < n else 0

                if rank[a] != rank[b] or a2 != b2:
                    new_rank += 1

                tmp[b] = new_rank

            rank, tmp = tmp, rank
            max_rank = new_rank

            if new_rank == n:
                break

            k *= 2

        # Inverse suffix array
        pos = [0] * n

        for i, x in enumerate(sa):
            pos[x] = i

        # Kasai LCP algorithm
        lcp = [0] * n
        h = 0

        for i in range(n):
            r = pos[i]

            if r == 0:
                continue

            j = sa[r - 1]

            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1

            lcp[r] = h

            if h:
                h -= 1

        # Minimum unique subarray
        ans = n

        for r in range(n):
            i = sa[r]

            left = lcp[r]
            right = lcp[r + 1] if r + 1 < n else 0

            length = max(left, right) + 1

            if i + length <= n:
                ans = min(ans, length)

        return ans
