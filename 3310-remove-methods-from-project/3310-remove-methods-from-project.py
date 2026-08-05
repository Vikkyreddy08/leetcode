from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        # Build adjacency list
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        # Find all suspicious methods
        suspicious = set()

        def dfs(node):
            if node in suspicious:
                return
            suspicious.add(node)
            for nei in graph[node]:
                dfs(nei)

        dfs(k)

        # Check whether any outside method calls a suspicious one
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        # Return remaining methods
        return [i for i in range(n) if i not in suspicious]