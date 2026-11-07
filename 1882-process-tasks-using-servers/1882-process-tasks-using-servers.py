
import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        n = len(servers)

        available = [(servers[i], i) for i in range(n)]
        heapq.heapify(available)

        busy = []
        ans = []

        time = 0

        for j, task in enumerate(tasks):

            # Current time cannot move backward
            time = max(time, j)

            # Release servers that have finished
            while busy and busy[0][0] <= time:
                end, weight, index = heapq.heappop(busy)
                heapq.heappush(available, (weight, index))

            # If all servers are busy, wait
            if not available:

                # Move to the earliest server finish time
                time = busy[0][0]

                # Release all servers that finish at this time
                while busy and busy[0][0] <= time:
                    end, weight, index = heapq.heappop(busy)
                    heapq.heappush(available, (weight, index))

            # Select server with smallest weight, then index
            weight, index = heapq.heappop(available)

            ans.append(index)

            # Calculate when this server becomes free
            finish = time + task

            heapq.heappush(
                busy,
                (finish, weight, index)
            )

        return ans
