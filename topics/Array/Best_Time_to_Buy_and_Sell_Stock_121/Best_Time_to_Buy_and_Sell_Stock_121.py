# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0

        cur_min = prices[0]
        max_diff = 0
        for i in range(1, len(prices)):
            cur_min = min(prices[i], cur_min)
            max_diff = max(prices[i] - cur_min, max_diff)

        return max_diff


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 5
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
# 0
print(solution.maxProfit([7, 6, 4, 3, 1]))
