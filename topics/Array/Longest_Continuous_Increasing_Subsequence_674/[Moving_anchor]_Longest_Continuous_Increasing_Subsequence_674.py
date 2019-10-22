# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        anchor = max_len = 0
        for i in range(len(nums)):
            if i and nums[i] <= nums[i - 1]:
                anchor = i
            max_len = max(i - anchor + 1, max_len)

        return max_len


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
# 1
print(solution.findLengthOfLCIS([2, 2, 2, 2, 2]))
