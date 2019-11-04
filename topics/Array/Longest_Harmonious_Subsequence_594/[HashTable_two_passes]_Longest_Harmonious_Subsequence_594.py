# https://leetcode.com/problems/longest-harmonious-subsequence/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(N)
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        num_count = {}

        for num in nums:
            num_count[num] = num_count.get(num, 0) + 1

        max_res = 0
        for num, count in num_count.items():
            if num + 1 in num_count:
                max_res = max(count + num_count[num + 1], max_res)

        return max_res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 5
print(solution.findLHS([1, 3, 2, 2, 5, 2, 3, 7]))
