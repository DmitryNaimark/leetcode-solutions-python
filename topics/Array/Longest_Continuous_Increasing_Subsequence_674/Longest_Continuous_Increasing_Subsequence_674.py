# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
# ---------------------------------------------------
from typing import List


# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        longest = cur = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                cur += 1
                longest = max(cur, longest)
            else:
                cur = 1

        return longest


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 3
print(solution.findLengthOfLCIS([1, 3, 5, 4, 7]))
# 1
print(solution.findLengthOfLCIS([2, 2, 2, 2, 2]))
