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
            results = (nums[i], cur_min * nums[i], cur_max * nums[i])
            cur_min = min(results)
            cur_max = max(results)

            max_product = max(cur_max, max_product)

        return max_product


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()

# 6
print(solution.maxProduct([2, 3, -2, 4]))
# 0
print(solution.maxProduct([-2,0,-1]))