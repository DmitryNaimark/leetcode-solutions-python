# https://leetcode.com/problems/maximum-subarray/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]

        for i in range(1, len(nums)):
            # Or, simply cur_sum += max(nums[i] + cur_sum, nums[i])
            if cur_sum < 0:
                cur_sum = 0
            cur_sum += nums[i]

            max_sum = max(cur_sum, max_sum)

        return max_sum


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 6
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
