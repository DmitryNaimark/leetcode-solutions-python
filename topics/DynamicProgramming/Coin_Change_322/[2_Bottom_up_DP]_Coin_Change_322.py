# https://leetcode.com/problems/coin-change/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(coins * amount)
# Space Complexity: O(amount) for memo.
# Idea: top-down iterative dynamic programming with memoization.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        return -1 if dp[amount] == float('inf') else dp[amount]


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.coinChange([1, 2, 5], 11))
# -1
print(solution.coinChange([2], 3))
