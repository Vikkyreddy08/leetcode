
from collections import deque
from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        dq = deque()
        cost = 0
        ans = 0

        j = n - 1

        for i in range(n - 1, -1, -1):
            # Merge smaller values into the current larger value
            while dq and nums[dq[-1]] < nums[i]:
                left = dq.pop()

                right = dq[-1] if dq else j + 1

                cost += (right - left) * (nums[i] - nums[left])

            dq.append(i)

            # Reduce the window until cost <= k
            while cost > k:
                cost -= nums[dq[0]] - nums[j]

                if dq[0] == j:
                    dq.popleft()

                j -= 1

            # Count valid subarrays ending between i and j
            ans += j - i + 1

        return ans
