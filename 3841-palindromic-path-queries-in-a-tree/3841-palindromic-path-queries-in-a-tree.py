
from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        parent[0] = 0
        order = [0]

        for u in order:
            for v in adj[u]:
                if v != parent[u]:
                    parent[v] = u
                    depth[v] = depth[u] + 1
                    order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            largest = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > largest:
                        largest = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            start, chain_head = stack.pop()
            u = start

            while u != -1:
                head[u] = chain_head
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        base = 1
        while base < n:
            base *= 2

        seg = [0] * (2 * base)
        chars = list(s)

        for u in range(n):
            seg[base + pos[u]] = 1 << (ord(chars[u]) - ord('a'))

        for i in range(base - 1, 0, -1):
            seg[i] = seg[2 * i] ^ seg[2 * i + 1]

        def range_xor(l, r):
            l += base
            r += base + 1
            result = 0

            while l < r:
                if l & 1:
                    result ^= seg[l]
                    l += 1
                if r & 1:
                    r -= 1
                    result ^= seg[r]
                l //= 2
                r //= 2

            return result

        def update(u, c):
            chars[u] = c
            i = base + pos[u]
            seg[i] = 1 << (ord(c) - ord('a'))
            i //= 2

            while i:
                seg[i] = seg[2 * i] ^ seg[2 * i + 1]
                i //= 2

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                update(int(parts[1]), parts[2])
            else:
                u, v = int(parts[1]), int(parts[2])
                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer
