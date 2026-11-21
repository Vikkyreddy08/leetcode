
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_children = [[] for _ in range(n)]

        last = {}

        def dfs(node):
            ch = s[node]
            old = last.get(ch)

            last[ch] = node

            new_parent = parent[node]

            if old is not None:
                new_parent = old

            if node != 0:
                new_children[new_parent].append(node)

            for child in children[node]:
                dfs(child)

            if old is None:
                del last[ch]
            else:
                last[ch] = old

        dfs(0)

        ans = [0] * n

        def calculate(node):
            ans[node] = 1

            for child in new_children[node]:
                ans[node] += calculate(child)

            return ans[node]

        calculate(0)

        return ans
