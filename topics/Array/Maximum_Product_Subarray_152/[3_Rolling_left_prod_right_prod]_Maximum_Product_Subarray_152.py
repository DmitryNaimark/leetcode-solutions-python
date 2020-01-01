# https://leetcode.com/problems/maximum-product-subarray/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)

        max_product = nums[0]
        prod_left = prod_right = 1

        for i in range(n):
            prod_left = (prod_left or 1) * nums[i]
            prod_right = (prod_right or 1) * nums[~i]

            max_product = max(prod_left, prod_right, max_product)

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
