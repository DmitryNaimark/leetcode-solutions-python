# https://leetcode.com/problems/longest-harmonious-subsequence/
# ---------------------------------------------------
from collections import Counter
from typing import List


# Runtime Complexity: O(N)
# Space Complexity: O(N), log N space is required by sorting in average case
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = Counter(nums)

        return max([num_count[num] + num_count[num + 1] for num in num_count if num_count[num + 1]], default=0)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 5
print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
# 20
print(solution.findLHS([2, 2, 2, 2, 2, 2, 2, 3, 1, 0, 0, 0, 3, 1, -1, 0, 1, 1, 0, 0, 1, 1, 2, 2, 2, 0, 1, 2, 2, 3, 2]))
# 2
print(solution.findLHS([1, 2, 3, 4]))
# 4
print(solution.findLHS([1, 2, 2, 1]))
