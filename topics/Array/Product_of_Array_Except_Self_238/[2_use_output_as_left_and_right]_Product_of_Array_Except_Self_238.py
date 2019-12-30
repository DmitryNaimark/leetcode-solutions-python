# https://leetcode.com/problems/product-of-array-except-self/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1), if we don't count the output array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        output = [0] * n
        output[0] = nums[0]
        for i in range(1, n):
            output[i] = output[i - 1] * nums[i]

        right_rolling_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] = right_rolling_prod
            if i > 0:
                output[i] *= output[i - 1]

            right_rolling_prod *= nums[i]

        return output


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [24, 12, 8, 6]
print(solution.productExceptSelf([1, 2, 3, 4]))
# [2, 3]
print(solution.productExceptSelf([3, 2]))