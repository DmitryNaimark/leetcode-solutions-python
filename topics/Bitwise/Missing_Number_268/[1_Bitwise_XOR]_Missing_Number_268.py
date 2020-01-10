# https://leetcode.com/problems/missing-number/
# ---------------------------------------------------
from typing import List

# Runtime Complexity: O(N)
# Space Complexity: O(1)
# Idea: XOR with all numbers in range [0, n] and XOR with all nums.
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        n = len(nums)
        for i in range(n):
            res ^= nums[i] ^ i

        return res


# ---------------------------------------------------
#                    Test Cases
# ---------------------------------------------------
solution = Solution()
# 2
print(solution.missingNumber([3, 0, 1]))
# 8
print(solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
# 1
print(solution.missingNumber([0]))
