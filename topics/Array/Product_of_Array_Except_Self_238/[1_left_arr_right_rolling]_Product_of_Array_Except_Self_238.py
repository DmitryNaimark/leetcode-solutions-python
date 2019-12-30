# https://leetcode.com/problems/product-of-array-except-self/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(N), to store additional left_prod array
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        left_prod = [0] * n
        left_prod[0] = nums[0]

        for i in range(1, n):
            left_prod[i] = left_prod[i - 1] * nums[i]

        output = [0] * n
        rolling_right_prod = 1
        for i in range(n - 1, -1, -1):
            output[i] = rolling_right_prod
            if i > 0:
                output[i] *= left_prod[i - 1]

            rolling_right_prod *= nums[i]

        return output


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# [24, 12, 8, 6]
print(solution.productExceptSelf([1, 2, 3, 4]))
# [2, 3]
print(solution.productExceptSelf([3, 2]))