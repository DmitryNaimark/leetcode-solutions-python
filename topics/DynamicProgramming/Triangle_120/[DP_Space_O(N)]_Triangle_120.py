# https://leetcode.com/problems/triangle/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(arithmetic_progression(rows)) => O(N^2)
# Space Complexity: O(rows)
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1:
            return triangle[0][0]

        rows = len(triangle)

        dp = triangle[rows - 1].copy()

        for r in range(rows - 2, -1, -1):
            for c in range(len(triangle[r])):
                dp[c] = min(dp[c], dp[c + 1]) + triangle[r][c]

        return dp[0]


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 11: 2 + 3 + 5 + 1
print(solution.minimumTotal([
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]))
