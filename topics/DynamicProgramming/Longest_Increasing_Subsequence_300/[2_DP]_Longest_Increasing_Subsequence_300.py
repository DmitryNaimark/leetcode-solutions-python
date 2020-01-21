# https://leetcode.com/problems/longest-increasing-subsequence/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(n^2) I think, because there are 2 branches with depth of n max.
# Space Complexity: O(n)
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(len(dp)):
            cur_num = nums[i]

            for j in range(i):
                if nums[j] < cur_num:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 4
print(solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
