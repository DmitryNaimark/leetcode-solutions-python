# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N) to heapify, O(N - 1) * (N * Log(N) * 3): iterations * (pop + pop + push) => O(N * log(N)),
# although the height of heap keeps decreasing, so maybe it's closer to O(N), similar to O(N) of heapify.
# Space Complexity: O(1)
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        while len(sticks) > 1:
            min1 = heapq.heappop(sticks)
            min2 = sticks[0]

            merged_stick = min1 + min2
            res += merged_stick
            heapq.heapreplace(sticks, merged_stick)

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 14: 2+3, 5+4
print(solution.connectSticks([2, 4, 3]))
# 30:
print(solution.connectSticks([2, 4, 3]))
# 8:
print(solution.connectSticks([1, 1, 1, 1]))
