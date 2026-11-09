class Solution:
    def busiestServers(self, k, arrival, load):
        n = len(arrival)

        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially, every server is available
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(server, value):
            pos = size + server
            tree[pos] = value

            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(left):
            if tree[1] == 0:
                return -1

            def search(node, start, end):
                if end < left or tree[node] == 0:
                    return -1

                if start == end:
                    return start

                mid = (start + end) // 2

                result = search(
                    node * 2, start, mid
                )

                if result != -1:
                    return result

                return search(
                    node * 2 + 1, mid + 1, end
                )

            return search(1, 0, size - 1)

        busy = []
        count = [0] * k

        import heapq

        for i in range(n):
            while busy and busy[0][0] <= arrival[i]:
                end_time, server = heapq.heappop(busy)
                update(server, 1)

            preferred = i % k

            server = find_first(preferred)

            if server == -1:
                server = find_first(0)

            if server == -1 or server >= k:
                continue

            update(server, 0)

            count[server] += 1

            heapq.heappush(
                busy,
                (arrival[i] + load[i], server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]