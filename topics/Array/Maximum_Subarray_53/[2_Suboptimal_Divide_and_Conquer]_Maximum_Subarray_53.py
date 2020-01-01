# https://leetcode.com/problems/maximum-subarray/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def cross_sum(self, nums, left, right, p):
        if left == right:
            return nums[left]

        left_subsum = float('-inf')
        curr_sum = 0
        for i in range(p, left - 1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)

        right_subsum = float('-inf')
        curr_sum = 0
        for i in range(p + 1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)

        return left_subsum + right_subsum

    def helper(self, nums, left, right):
        if left == right:
            return nums[left]

        mid = (left + right) // 2

        left_sum = self.helper(nums, left, mid)
        right_sum = self.helper(nums, mid + 1, right)
        cross_sum = self.cross_sum(nums, left, right, mid)

        return max(left_sum, right_sum, cross_sum)

    def maxSubArray(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 6: [4, -1, 2, 1]
print(solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
