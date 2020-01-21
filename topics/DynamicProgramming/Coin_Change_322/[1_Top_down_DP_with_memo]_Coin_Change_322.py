# https://leetcode.com/problems/coin-change/
# ---------------------------------------------------
from collections import deque
from typing import List

# Runtime Complexity: O(coins * amount)
# Space Complexity: O(amount) for memo.
# Idea: top-down iterative dynamic programming with memoization.
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_steps = float('inf')

        q = deque()

        # remaining: steps
        memo = {}

        # (amount_left, steps_taken)
        q.append((amount, 0))
        while q:
            remaining, steps = q.popleft()

            if remaining == 0:
                min_steps = min(steps, min_steps)

            if steps >= memo.get(remaining, float('inf')):
                continue

            memo[remaining] = steps

            for coin in coins:
                if remaining - coin >= 0:
                    q.append((remaining - coin, steps + 1))

        # print(memo)
        return -1 if min_steps == float('inf') else min_steps


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.coinChange([1, 2, 5], 11))
# -1
print(solution.coinChange([2], 3))
