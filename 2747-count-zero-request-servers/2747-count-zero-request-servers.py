
class Solution:
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda log: log[1])

        sorted_queries = sorted(
            enumerate(queries),
            key=lambda item: item[1]
        )

        ans = [0] * len(queries)

        active = {}
        count = 0

        left = 0
        right = 0

        for index, q in sorted_queries:
            start = q - x

            # Add requests up to the query time
            while right < len(logs) and logs[right][1] <= q:
                server = logs[right][0]

                if server not in active:
                    active[server] = 0
                    count += 1

                active[server] += 1
                right += 1

            # Remove requests before the window
            while left < right and logs[left][1] < start:
                server = logs[left][0]

                active[server] -= 1

                if active[server] == 0:
                    del active[server]
                    count -= 1

                left += 1

            # Servers with zero requests
            ans[index] = n - count

        return ans
