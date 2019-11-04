# https://leetcode.com/problems/longest-harmonious-subsequence/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(N * log(N))
# Space Complexity: O(log(N)), log N space is required by sorting in average case
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        nums.sort()

        prev_count = cur_count = max_res = 0

        for i in range(len(nums)):
            if i == 0 or nums[i] == nums[i - 1]:
                cur_count += 1
            else:
                prev_count = cur_count if (nums[i - 1] + 1 == nums[i]) else 0
                cur_count = 1

            if prev_count > 0:
                max_res = max(prev_count + cur_count, max_res)

        return max_res


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
