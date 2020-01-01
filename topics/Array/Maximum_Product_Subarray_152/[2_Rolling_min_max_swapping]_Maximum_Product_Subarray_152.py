# https://leetcode.com/problems/maximum-product-subarray/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_product = nums[0]
        cur_min = nums[0]
        cur_max = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                cur_min, cur_max = cur_max, cur_min

            # Since nums[i] is less than 0, min will become max and max will become min.
            cur_min, cur_max = min(cur_min * nums[i], nums[i]), max(cur_max * nums[i], nums[i])

            max_product = max(cur_max, max_product)

        return max_product


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()

# 6
print(solution.maxProduct([2, 3, -2, 4]))
# 0
print(solution.maxProduct([-2, 0, -1]))
# 2
print(solution.maxProduct([0, 2]))
