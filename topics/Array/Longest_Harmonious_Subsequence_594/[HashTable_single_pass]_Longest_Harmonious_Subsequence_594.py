# https://leetcode.com/problems/longest-harmonious-subsequence/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = {}

        max_res = 0
        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

            if num + 1 in num_count:
                max_res = max(num_count[num] + num_count[num + 1], max_res)
            if num - 1 in num_count:
                max_res = max(num_count[num] + num_count[num - 1], max_res)

        return max_res



# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 5
# print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
# 20
print(solution.findLHS([2, 2, 2, 2, 2, 2, 2, 3, 1, 0, 0, 0, 3, 1, -1, 0, 1, 1, 0, 0, 1, 1, 2, 2, 2, 0, 1, 2, 2, 3, 2]))
# 2: 7
